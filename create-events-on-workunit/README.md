# Create Event(s) on WU

This tool quickly creates Play and Stop events for the sounds or containers you select in Wwise. A search window pops up so you can choose exactly where the new events should go.

## Features

*   **Automatic Event Creation**: Instantly makes a Play event for any selected sound.
*   **Handles Looping Sounds**: If you select a looping container, it automatically creates a matching Stop event as well.
*   **Choose Your Work Unit**: A simple search box lets you find the exact Event Work Unit to place your new events in.
*   **Safe to Use**: All changes can be undone with a single "Undo" (Ctrl+Z) in Wwise.

## Installation

1.  **Complete General Setup**: Make sure you have followed all the steps in the main [Installation Guide](../../README.md).
2.  **Ready to Go**: No other setup is needed for this tool.

## Usage

1.  In your Wwise project, select one or more sounds or containers.
2.  Right-click the selection, go to the `waapi-tools` menu, and choose `Create Event(s) on WU`.
3.  A search window will appear. Start typing the name of the Event Work Unit where you want to add the new events.
4.  Click on the Work Unit you want from the list, or press `Enter` to select the first one.
5.  The tool will instantly create the events in that location.