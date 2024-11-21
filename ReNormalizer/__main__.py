from waapi import WaapiClient
from pprint import pprint
import argparse
from waapi_helpers.waapi_helpers import get_selected
from ui_components.app import App

try:
    # Define arguments for the script
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('ids', metavar='GUID', nargs='*', help='')

    args = parser.parse_args()
    selected = []


    selected = get_selected(args)

    # app frame
    app = App(selected=selected)
    app.mainloop()
except Exception as e:
    print(e)