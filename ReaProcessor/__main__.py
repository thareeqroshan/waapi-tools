import os
import sys
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox
from waapi import WaapiClient, CannotConnectToWaapiException
from waapi_helpers.waapi_helpers import get_selected
import subprocess
import argparse
import shutil

reaper_path = Path("C:/Program Files/REAPER (x64)/reaper.exe")

def get_repository_path() -> str:
    current_path = os.path.abspath(__file__)
    
    # go back a folder until we find the .git folder
    while current_path != os.path.dirname(current_path):
        if os.path.isdir(os.path.join(current_path, '.git')):
            return current_path
        current_path = os.path.dirname(current_path)

    return ''
originals_path = os.path.join(get_repository_path(), 'WwiseProject/Originals/SFX')

def copy_folders_recursively(source_folder, destination_folder ) -> int:
    error_code = 0
    error_log_file = os.path.join(source_folder, 'error_log.txt')
    # clear the error log file
    with open(error_log_file, 'w') as f:
        f.write('')
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(destination_folder, os.path.relpath(src_file, source_folder))
            dest_folder = os.path.dirname(dest_file)
            if not os.path.exists(dest_folder):
                # add the folder to the error log file
                with open(error_log_file, 'a') as f:
                    f.write(f'Creating folder: {dest_folder}\n')
                os.makedirs(dest_folder)
            try:
                os.system(f'copy "{src_file}" "{dest_file}"')
            except Exception as e:
                print(f'Error: {e}')
                # append the error to the error log file
                with open(error_log_file, 'a') as f:
                    f.write(f'Error: {e}\n')

                error_code = 1
    return error_code


def connect_to_wwise():
    try:
        client = WaapiClient()
        print("Connected to Wwise")
        return client
    except CannotConnectToWaapiException:
        print("Could not connect to Wwise")
        return None

def get_selected_objects(client):
    options = {'return': ['id', 'name', 'type', 'originalFilePath']}
    result = client.call("ak.wwise.ui.getSelectedObjects", options=options)
    return result.get("objects", [])

def select_reaper_fx_chain():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Reaper FX Chain", "*.RfxChain")])
    return file_path

def create_batch_converter_config(audio_files, fx_chain, output_dir):
    config_lines = []
    for audio_file in audio_files:
        input_path = Path(audio_file)
        output_path = output_dir / f"{input_path.stem}_processed{input_path.suffix}"
        config_lines.append(f'FILE 0 "{input_path}" "{output_path}"')
    
    config_block = f'''<CONFIG
RIPPLE 0
FXCHAIN "{fx_chain}"
>'''
    config_lines.append(config_block)
    return config_lines

def apply_reaper_fx(audio_files, fx_chain, output_dir):
    current_dir = Path(__file__).parent
    csv_file = current_dir / 'audio_files.txt'
    if csv_file.exists():
        csv_file.unlink()
    converted_path = os.path.join(current_dir, 'converted')
    converted_path = output_dir 


    with open(csv_file, 'w') as f:
        for audio_file in audio_files:
            audio_file_folder = os.path.dirname(audio_file)
            relative_path = os.path.relpath(audio_file_folder, originals_path)
            output_folder = os.path.join(converted_path, relative_path)
            if audio_file_folder == originals_path:
                output_folder = converted_path
            output_file = os.path.join(output_folder, os.path.basename(audio_file))
            f.write(audio_file + '\t' + output_file + '\n')
        config_block = f'''<CONFIG
SRATE 48000
OUTPATH '{output_dir}'
RSMODE 10,
FXCHAIN "{fx_chain}"
OUTPATTERN $item
>'''
        f.write(config_block)
    batch_convert_files = '"' + f'{reaper_path}' + '" ' + f'-batchconvert {csv_file}'
    output = os.system(batch_convert_files)
    print(output)
    error_code = copy_folders_recursively(converted_path, originals_path)
    shutil.rmtree(converted_path)

        # batch_convert_command = [str(reaper_path), "-batchconvert", str(input_path), str(output_path), "-fxchain", str(fx_chain)]
        # try:
        #     result = subprocess.run(batch_convert_command, check=True, capture_output=True, text=True)
        #     print("Batch conversion completed successfully")
        #     print(f"Reaper output: {result.stdout}")
        # except subprocess.CalledProcessError as e:
        #     print(f"Error during batch conversion: {e}")
        #     print(f"Reaper output: {e.output}")
    
    # config_lines = create_batch_converter_config(audio_files, fx_chain, output_dir)
    
    # with open(csv_file, 'w') as f:
    #     f.write('\n'.join(config_lines))
    
    # batch_convert_command = [str(reaper_path), "-batchconvert", str(csv_file)]
    # try:
    #     result = subprocess.run(batch_convert_command, check=True, capture_output=True, text=True)
    #     print("Batch conversion completed successfully")
    #     print(f"Reaper output: {result.stdout}")
    # except subprocess.CalledProcessError as e:
    #     print(f"Error during batch conversion: {e}")
    #     print(f"Reaper output: {e.output}")

def main():
    parser = argparse.ArgumentParser(description='Apply Reaper FX Chains to multiple sound SFX objects in Wwise')
    parser.add_argument('ids', metavar='GUID', nargs='*', help='One or many guid of the form {01234567-89ab-cdef-0123-4567890abcde}. The script retrieves the current selected if no GUID specified.')

    args = parser.parse_args()
    selected_objects = []
    selected_objects = get_selected(args)
    # client = connect_to_wwise()
    # if not client:
    #     return

    # selected_objects = get_selected_objects(client)
    # if not selected_objects:
    #     messagebox.showinfo("No Selection", "No objects selected in Wwise")
    #     return

    # print(selected_objects)

    # fx_chain = ""
    fx_chain = select_reaper_fx_chain()
    if not fx_chain:
        messagebox.showinfo("No FX Chain", "No FX chain selected")
        return

    output_dir = Path(__file__).parent / 'processed'
    output_dir.mkdir(exist_ok=True)
    
    audio_files = [obj['originalFilePath'] for obj in selected_objects]
    print(output_dir)
    
    if not audio_files:
        messagebox.showinfo("No Audio Files", "No audio files selected in Wwise")
        return

    apply_reaper_fx(audio_files, fx_chain, output_dir)
    
    # # client.disconnect()
    # messagebox.showinfo("Process Completed", "FX application completed. Processed files are in the 'processed' folder.")

if __name__ == "__main__":
    main()
