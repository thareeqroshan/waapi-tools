from waapi import WaapiClient
from pprint import pprint
import traceback


def get_descendants(parent_id, parent_path):
    try:
        # Connect to Wwise
        with WaapiClient() as client:
            query = {
                "from": {"id": [parent_id]},
                "transform": [{"select": ["descendants"]}]
            }
            waql_query = f"from object {parent_path}"
            options = { "return" : ["path", "id", "isPlayable", "name"] }
            descendants = client.call("ak.wwise.core.object.get", query, options=options)['return']
            return descendants['return']
    except Exception as e:
        traceback.print_exc()
        print(str(e))



def get_selected(args,):
    try:
        # Connect to Wwise
        with WaapiClient() as client:
            
            options = { "return" : ["path", "id", "isPlayable", "name", "originalFilePath"] }

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

            return selected

    except Exception as e:
        traceback.print_exc()
        print(str(e))