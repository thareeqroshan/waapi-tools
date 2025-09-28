# WAAPI Tools for Wwise

This repository is a collection of Python-based tools that use the Wwise Authoring API (WAAPI) to automate common tasks inside Audiokinetic Wwise. These tools are designed for sound designers and require no programming knowledge to install and use.

## Installation Guide

Follow these steps carefully to set up the tools.

---

### Step 1: Install Python

If you don't have Python installed, you'll need to install it first.

1.  **Download Python**: Go to the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2.  Download the latest version of Python 3 (any version 3.6 or newer will work).
3.  **Run the Installer**: Open the downloaded installer.
4.  **IMPORTANT**: On the first screen of the installer, make sure to check the box that says **"Add Python to PATH"** at the bottom. This step is crucial for the tools to work correctly.
    ![Add Python to PATH](https_i.imgur.com_7v5p4XF.png)
5.  Click **"Install Now"** and follow the on-screen prompts to complete the installation.

---

### Step 2: Download and Unzip the Tools

1.  Click the green **"< > Code"** button at the top of this page.
2.  Select **"Download ZIP"** from the dropdown menu.
3.  Save the ZIP file to your computer and unzip it to a location you'll remember, such as your Desktop or Documents folder.

---

### Step 3: Install Required Dependencies

Next, you need to install the Python libraries that these tools depend on.

1.  **Open Command Prompt**:
    *   Press the **Windows Key** (or click the Start Menu).
    *   Type `cmd` and press **Enter**. This will open the Command Prompt window.
2.  **Navigate to the Tool Folder**:
    *   In the Command Prompt, type `cd` followed by a space.
    *   Drag the unzipped tool folder (the one named `waapi-tools-main` or similar) from your file explorer and drop it into the Command Prompt window. The path to the folder will appear automatically.
    *   Press **Enter**. The command prompt should now be "inside" the tool folder.
3.  **Install Dependencies**:
    *   Type the following command exactly as it appears below and press **Enter**:
        ```
        pip install -r pip-requirements.txt
        ```
    *   This command tells Python's package manager (`pip`) to read the `pip-requirements.txt` file and automatically install all the necessary libraries. You will see text in the command prompt as the libraries are downloaded and installed.

---

### Step 4: Enable Wwise Authoring API (WAAPI)

For the tools to communicate with Wwise, you must enable the Wwise Authoring API.

1.  Open your Wwise project.
2.  Go to the **Project** menu and select **User Preferences**.
3.  In the User Preferences window, check the box next to **"Enable Wwise Authoring API"**.
    ![Enable WAAPI](https_i.imgur.com_jX3sY8W.png)
4.  Click **OK**.

---

## Tool Usage

Your tools are now installed and ready to use! To use a specific tool, right-click an object in Wwise, and you will see a "waapi-tools" context menu.

For detailed instructions on what each tool does and how to use it, please refer to the `README.md` file inside each tool's sub-folder:

*   **[ReNormalizer](ReNormalizer/README.md)**: Re-Normalizes your sounds in Wwise.
*   **[ReaProcessor](ReaProcessor/README.md)**: Batch Reaper FX Chain Utility for Wwise.
*   **[Create Event(s) on WU](create-events-on-workunit/README.md)**: Creates events for the selected object(s).