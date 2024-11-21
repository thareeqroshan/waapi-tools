from waapi import WaapiClient
from pprint import pprint
from pathlib import Path
import argparse, traceback
from ui_components.imgui_search_field import SearchComponent, WIDTH, HEIGHT
import dearpygui.dearpygui as dpg
import math

# Define arguments for the script
parser = argparse.ArgumentParser(description='Automatically create new play events from the selection and replicate the work unit hierarchy.')
parser.add_argument('ids', metavar='GUID', nargs='*', help='One or many guid of the form {01234567-89ab-cdef-0123-4567890abcde}. The script retrieves the current selected if no GUID specified.')

args = parser.parse_args()
selected = []

def isContainerLoopable(container_name):
    # Check if the container is loopable
    query = {
        "from": {"id": [container_name]}
    }
    options = {
        "return": ["name", "id", "type", "path", "IsLoopingEnabled","PlayMechanismLoop"]
    }
    container = client.call("ak.wwise.core.object.get", query, options=options)['return'][0]
    if container.get("PlayMechanismLoop") is not None:
        return container["PlayMechanismLoop"]
    elif container.get("IsLoopingEnabled") is not None:
        return container["IsLoopingEnabled"]
    return False

def create_event(parent, name, target, action_id=1):
    # Create an Event withe specified name and target
    return {
        "type":"Event",
        "name":name,
        "children":[
            {
                "type":"Action",
                "name": "",
                "@Target": target,
                "@ActionType": action_id
            }
        ]
    }

def create_workunit(name):
    # Create a Work Unit with the specified name
    return {
        "type":"WorkUnit",
        "name": name
    }

def create_virtual_folder(name):
    # Create a Virtual Folder with the specified name
    return {
        "type":"Folder",
        "name": name
    }

def add_events_to_first_event(sender, app_data, user_data):
    temp = ""
    for value in search_component.string_values:
        if dpg.is_item_visible(value):
            temp = value
            break

    add_events(sender, app_data, [user_data, temp])

def add_events(sender, app_data, user_data):
    selected, parent = user_data
    client.call("ak.wwise.core.undo.beginGroup", {})

    for obj in selected:
        name = obj['name']
        id = obj['id']
        set_args = {
            "objects": [],
            "onNameConflict": "merge",
        }
        play_event = create_event(parent, name+"_Play", id)
        set_args["objects"].append(
            {
                "object": parent,
                "children": [play_event]
            }
        )
        
        if isContainerLoopable(id):
            print(f"Container '{id}' is loopable")
            stop_event = create_event(parent, name+"_stop", id, action_id=2)

            set_args["objects"].append(
                {
                    "object": parent,
                    "children": [stop_event]
                }
            )
        result = client.call("ak.wwise.core.object.set", set_args)
    #stop the undo group
    client.call("ak.wwise.core.undo.endGroup", {"displayName": "Create Events on WU"})
    dpg.stop_dearpygui()


try:
    # Connect to Wwise
    with WaapiClient() as client:
        
        options = { "return" : ["path", "id", "isPlayable", "name"] }

        # if no ID is passed as argument, use the selected object from the project
        if args.ids is None or len(args.ids) == 0:
            selected  = client.call("ak.wwise.ui.getSelectedObjects", {}, options=options)['objects']
        else:
            ids_list = ', '.join(f'"{item}"' for item in args.ids)
            selected  = client.call("ak.wwise.core.object.get", { "waql":f"$ {ids_list}" }, options=options)['return']

        set_args = {
            "objects": [],
            "onNameConflict": "merge",
        }

        # get all event work units as a list
        events_get_args = {
            "waql": r"from type workunit"
        }
        event_work_units = client.call("ak.wwise.core.object.get", events_get_args, options=options)
        event_list = [event["path"]for event in event_work_units['return'] if event["path"].startswith("\\Events\\")]
        dpg.create_context()
        dpg.create_viewport(title="Search Example", width=WIDTH, height=200, x_pos=500, y_pos=500,decorated=False, resizable=False)
        dpg.setup_dearpygui()

        with dpg.window(label="Search Window", id="Primary Window",  no_resize=True, no_move=True, no_close=True, no_collapse=True, no_title_bar=True): # , no_resize=True, no_move=True, no_close=True, no_collapse=True, no_title_bar=True, autosize=True
            search_component = SearchComponent(event_list, width=WIDTH, callback=add_events, user_data=selected)
        search_component.focus()
        with dpg.handler_registry():
            dpg.add_key_press_handler(dpg.mvKey_Escape, callback=lambda: dpg.stop_dearpygui())
            dpg.add_key_press_handler(dpg.mvKey_Return, callback=add_events_to_first_event, user_data=selected)

        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

except Exception as e:
    traceback.print_exc()
    print(str(e))