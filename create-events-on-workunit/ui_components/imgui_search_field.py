import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

# Set global variables for width and height
WIDTH = 500
HEIGHT = 600

# Creates a search component that can be used to search a list of strings.
# The component is created with the following items:
# 1. A text input field
# 2. A filter set that will filter the results based on the text input
# 3. A button for each string value in the list of strings passed to the component
# The component can be passed a parent widget, which will be used as the parent for all of the component's widgets.
# The component can be focused, which will set the focus to the text input field.
# The component has a callback for when the text input field is changed, which will update the filter set.
# The component has a callback for when a search result is selected, which will set the text input field to the selected value.

class SearchComponent:
    def __init__(self, values, parent=None, input_text_changed_callback = None, **kwargs):
        self.string_values = values
        self.parent = parent
        self.filter_id = dpg.generate_uuid()
        self.search_id = dpg.generate_uuid()
        self.width = kwargs['width']
        self.height = kwargs['height'] if kwargs.get('height') else 100
        self.callback_function = self.input_text_callback if kwargs.get('callback') is None else kwargs['callback']
        self.callback_user_data = None if kwargs.get('user_data') is None else kwargs['user_data']
        self.viewport_height = kwargs['height'] if kwargs.get('height') else 100
        self.create_component()

    def select_result(self, sender, app_data, user_data):
        test_args = {
            "item": self.search_id,
            "value": user_data
        }
        try:
            dpg.set_value(**test_args)
        except Exception as error:
            print("An error occurred:", type(error).__name__, "–", error)

    def input_text_callback(self, sender, app_data, user_data):
        test_args = {
            "item": user_data,
            "value": app_data
        }
        try:
            dpg.set_value(**test_args)
            counter = 0
            for value in self.string_values:
                counter +=1
            # dpg.set_viewport_height((counter) * int(HEIGHT/20))
            # if self.input_text_changed_callback is not None:
            #     self.input_text_changed_callback((counter) * int(HEIGHT/20))
        except Exception as error:
            print("An error occurred:", type(error).__name__, "–", error)
    
    def get_viewport_height(self):
        return dpg.get_viewport_height()

    def create_component(self):
        input_text_kwargs = {
            "label": "Search",
            "tag": self.search_id,
            "callback": self.input_text_callback,
            "user_data": self.filter_id,
            "width": self.width
        }
        filter_field_kwargs = {
            "tag": self.filter_id
        }
        if self.parent is not None:
            input_text_kwargs["parent"] = self.parent
            filter_field_kwargs["parent"] = self.parent

        dpg.add_input_text(**input_text_kwargs)
        with dpg.theme() as theme_id:
            with dpg.theme_component(dpg.mvInputText):
                gray = 0.4
                color = (gray * 255, gray * 255, gray * 255)
                dpg.add_theme_color(dpg.mvThemeCol_FrameBg, color, category=dpg.mvThemeCat_Core)
        dpg.bind_item_theme(self.search_id, theme_id)
        with dpg.filter_set(**filter_field_kwargs):
            for value in self.string_values:
                dpg.add_button(tag=value, label=value, filter_key=value, callback=self.callback_function, user_data=[self.callback_user_data, value], width=self.width, height = int(HEIGHT/20))
    def focus(self):
        dpg.focus_item(self.search_id)


if __name__ == "__main__":
    string_values = ["Value1", "Value2", "Value3", "test", "test2", "value4","value5"]

    dpg.create_context()
    dpg.create_viewport( title="Search Example", width=WIDTH, height=(len(string_values) + 2)*int(HEIGHT/20), x_pos=500, y_pos=500, decorated=False, resizable=False)
    dpg.setup_dearpygui()


    with dpg.window(label="Search Window", id="main_window", width=WIDTH,  no_resize=True, no_move=True, no_close=True, no_collapse=True, no_title_bar=True, autosize=True): # , no_resize=True, no_move=True, no_close=True, no_collapse=True, no_title_bar=True, autosize=True
        search_component = SearchComponent(string_values, width=WIDTH)
    search_component.focus()
    with dpg.handler_registry():
        dpg.add_key_press_handler(dpg.mvKey_Escape, callback=lambda: dpg.stop_dearpygui())

    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
