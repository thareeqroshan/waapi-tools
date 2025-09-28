# ReNormalizer

ReNormalizer is a tool to change the peak volume of audio files in your Wwise project. It gives you a simple window where you can see the current peak level and set a new one.

## Features

*   **Peak Normalization**: Set a new peak volume (in decibels) for your audio files.
*   **Live Feedback**: The tool shows you the current peak value for each selected file.
*   **Simple Slider**: Use a slider to easily set the new peak level you want.
*   **Batch Processing**: Normalize many audio files at the same time.

## Installation

1.  **Complete General Setup**: Make sure you have followed all the steps in the main [Installation Guide](../../README.md).
2.  **Ready to Go**: No other setup is needed for this tool.

## Usage

1.  In your Wwise project, select one or more audio files you want to normalize.
2.  Right-click the selection, go to the `waapi-tools` menu, and choose `Re-Normalize your sounds`.
3.  A window will open, showing the selected files and their peak values.
4.  Use the slider to choose the new target peak level.
5.  Click the "Normalize" button.
6.  The files will be processed, and you will see the peak values update in the window.