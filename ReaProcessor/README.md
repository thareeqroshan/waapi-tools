# ReaProcessor

ReaProcessor is a tool that lets you use your favorite Reaper FX Chains on audio files directly within your Wwise project.

## Features

*   **Batch Processing**: Apply a single FX Chain to many audio files at once.
*   **Direct Integration**: Automatically modifies the original audio files in your Wwise project.
*   **Easy FX Selection**: A file dialog helps you find and select your saved Reaper FX Chains (`.RfxChain` files).

## Installation

This tool requires one-time manual setup to connect with your Reaper installation.

1.  **Complete General Setup**: Make sure you have followed all the steps in the main [Installation Guide](../../README.md).
2.  **Install Reaper**: This tool requires a local installation of [Cockos REAPER](https://www.reaper.fm/download.php).
3.  **Link Your Reaper Installation**: You must tell the tool where to find Reaper on your computer.

    *   **a. Find your `reaper.exe` file.** This is usually located in `C:\Program Files\REAPER (x64)`. Right-click the REAPER shortcut on your desktop and select "Open file location" to find it easily.
    *   **b. Copy the file path.** In the folder that opens, right-click the `reaper.exe` file and select "Copy as path".
    *   **c. Open the script file.** Navigate to the `ReaProcessor` folder inside your `waapi-tools` directory and open the `__main__.py` file with a simple text editor like Notepad.
    *   **d. Edit the path.** Find the line that starts with `reaper_path =`. Paste the path you copied. **IMPORTANT:** Make sure to remove the quotes and use forward slashes (`/`) instead of backslashes (`\`).

    **Example:**

    If you copied this path: `"C:\Program Files\REAPER (x64)\reaper.exe"`

    You should change the line in the file to look like this:
    `reaper_path = Path("C:/Program Files/REAPER (x64)/reaper.exe")`

    *   **e. Save and close the file.**

## Usage

1.  In your Wwise project, select one or more audio files you want to process.
2.  Right-click the selection, go to the `waapi-tools` menu, and choose `Batch Reaper FX Chain Utility for Wwise`.
3.  A file dialog will open. Find and select the Reaper FX Chain (`.RfxChain`) you want to apply.
4.  The tool will process the files in the background. The original files in Wwise will be overwritten with the new, processed versions.