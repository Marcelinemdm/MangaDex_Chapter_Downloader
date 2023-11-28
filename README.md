## README

### MangaDex Chapter Image Downloader (include)

This Python script allows you to obtain the image URLs for a specific manga chapter on Mangadex without downloading the images. The script prompts the user to input the manga name and chapter ID and then generates an HTML file containing image tags with the corresponding URLs. The HTML file is styled using the provided CSS code.

#### Instructions:

1. **Requirements:**
   - Python
   - Requests library (install using `pip install requests`)

2. **How to Use:**
   - Run the script.
   - Enter the manga name and chapter ID when prompted.
   - The script will generate an HTML file in the specified output directory (`projeto` in this example).

3. **Notes:**
   - Make sure to customize the CSS code according to your styling preferences.
   - Adjust the `output_directory` variable to your desired output path.
   - **Important:** This script may not work in some instances due to Mangadex's policies. However, the URL used in the generated HTML's `src` attribute contains the chapter information.

### MangaDex Chapter Image Downloader (noninclude)

This Python script allows you to download the images for a specific manga chapter from Mangadex. The script prompts the user to input the manga name and chapter ID, and it creates a folder structure to store the downloaded images. Additionally, it generates an HTML file with image tags referencing the downloaded images.

#### Instructions:

1. **Requirements:**
   - Python
   - Requests library (install using `pip install requests`)
   - pyperclip library (install using `pip install pyperclip`)
   - tkinter library (included with Python, additional installation may be required on some systems)

2. **How to Use:**
   - Run the script.
   - Enter the manga name and chapter ID when prompted.
   - The script will download the chapter images into a folder structure and create an HTML file referencing these images.
   - The folder structure is created in the specified output directory (`projeto` in this example).

3. **Notes:**
   - Make sure to customize the CSS code according to your styling preferences.
   - Adjust the `output_directory` variable to your desired output path.

**Important Note:**
The HTML and CSS for the `/home` page have not been tested and will likely need adjustments by the user.

### MangaDex Manga ID Finder (search)

This Python script allows you to find the MangaDex IDs for a specific manga title. The script prompts the user to input the manga title and then queries the MangaDex API to retrieve the manga IDs.

#### Instructions:

1. **Requirements:**
   - Python
   - Requests library (install using `pip install requests`)
   - pyperclip library (install using `pip install pyperclip`)
   - tkinter library (included with Python, additional installation may be required on some systems)

2. **How to Use:**
   - Run the script.
   - Enter the manga title when prompted.
   - The script will query the MangaDex API and display the manga IDs.
   - Use the "Copy IDs" button to copy the IDs to the clipboard.

3. **Note:**
   - The `tkinter` library is used for the graphical user interface.