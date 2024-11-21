import customtkinter
from audio.normalise import normalize_audio_file, get_peak_amplitude

class FileView(customtkinter.CTkScrollableFrame):
    widgets = []
    def __init(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky="nsew")
        self._desired_height = 0
    
    def create_widgets(self, selected):
        row_number = 0
        try:
            for obj in selected:
                file_name_label = customtkinter.CTkLabel(master=self, text=obj['name'], bg_color="#444", justify="left")
                file_name_label.grid(row=row_number, column=0, padx=10, pady=10)
                peak_value_lavel = customtkinter.CTkLabel(master=self, text=f"Peak: {get_peak_amplitude(obj['originalFilePath']):.2f}", bg_color="#444", justify="left")
                peak_value_lavel.grid(row=row_number, column=1, padx=10, pady=10)
                self.widgets.append(file_name_label)
                self.widgets.append(peak_value_lavel)
                row_number += 1
        except Exception as e:
            print(e)

    def clear_widgets(self):
        try:
            for widget in self.widgets:
                widget.destroy()
            self.widgets = []
        except Exception as e:
            print(e)


class App(customtkinter.CTk):
    def __init__(self,selected):
        super().__init__()
        self.selected = selected

        self.button = customtkinter.CTkButton(self, text="Normalize", command=self.button_callback)
        self.button.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.peak_slider = customtkinter.CTkSlider(self, from_=-20, to=0,number_of_steps=20,  command=self.slider_callback)
        self.peak_slider.set(-6)
        self.peak_slider_label = customtkinter.CTkLabel(self, text="Peak: -6.0")
        self.peak_slider_label.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="ew")
        self.peak_slider.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="ew")
        # self.set_appearance_mode("System")  # Modes: system (default), light, dark
        # self.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

        self.title("ReNormalizer")
        self.geometry("400x600")
        self.grid_columnconfigure(0, weight=1)
        
        self.fileView = FileView(master=self, height=400)
        self.fileView.grid(row=2, column=0,  columnspan=2,sticky="nsew")
        self.fileView.create_widgets(selected)

    
    def slider_callback(self, value):
        self.peak_slider_label.configure(text=f"Peak: {value}")
              
    def button_callback(self):
        try:
            for obj in self.selected:
                # print(obj['name'])
                normalize_audio_file(obj['originalFilePath'],obj['originalFilePath'],target_loudness=self.peak_slider.get())
            self.fileView.clear_widgets()
            self.fileView.create_widgets(self.selected)
        except Exception as e:
            print(e)
