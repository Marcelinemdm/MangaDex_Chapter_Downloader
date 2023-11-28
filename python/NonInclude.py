import os
import requests
import tkinter as tk
from tkinter import filedialog

def download_chapter(manga_name, chapter_id, output_directory):
    folder_path = os.path.join(output_directory, manga_name, f"capitulo {chapter_id}")
    os.makedirs(folder_path, exist_ok=True)

    chapter_info = requests.get(f"https://api.mangadex.org/at-home/server/{chapter_id}").json()
    host = chapter_info['baseUrl']
    chapter_hash = chapter_info['chapter']['hash']
    data = chapter_info['chapter']['data']

    for page in data:
        r = requests.get(f"{host}/data/{chapter_hash}/{page}")

        with open(os.path.join(folder_path, page), mode="wb") as f:
            f.write(r.content)

    print(f"Downloaded {len(data)} pages.")
    return folder_path

def create_html(folder_path):
    css_code = '''
    body {
      margin: 0;
      font-family: Arial, sans-serif;
      background: linear-gradient(to right, #101d42, #0d1317);
      color: #ffffff;
    }

    header {
      padding: 10px;
      width: 1050px;
      margin: auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    header img {
      max-width: 100%;
      height: auto;
    }

    main {
      padding: 10px;
    }

    main.bg-blueglobal1900 {
      width: 1050px;
      margin: 15px auto;
      border-radius: 25px;
    }

    footer {
      padding: 10px;
      text-align: center;
      color: white;
      position: fixed;
      bottom: 0;
      width: 100%;
    }

    /* Adição para tornar o design responsivo */
    @media (max-width: 1150px) {
      .main.bg-blueglobal1900 {
        width: 90%;
      }
    }
    '''

    html_base = f'''
    <!DOCTYPE html>
    <html lang="en, pt-br">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>TQ</title>
      <link rel="shortcut icon" href="/home/logo.png" type="image/x-icon">
      <style>
        {css_code}
      </style>
    </head>
    <body>
      <header>
        <a href="/home/"><img src="/logo.png" alt="logo"></a>
      </header>
      <main class="bg-blueglobal1900">
    '''

    for page in os.listdir(folder_path):
        html_base += f'''
          <img src="{page}" alt="page" style="height: 630px; display: block; margin: 0 auto;">
        '''

    html_base += '''
      </main>
      <footer>
        <p>© 2023 - Todos os direitos reservados.</p>
      </footer>

      <script src="/home/script.js"></script>
    </body>
    </html>
    '''

    with open(f"{folder_path}/index.html", mode="w", encoding="utf-8") as html_file:
        html_file.write(html_base)

def on_download_button_click():
    manga_name = manga_name_entry.get()
    chapter_id = chapter_id_entry.get()
    output_directory = filedialog.askdirectory()

    if manga_name and chapter_id and output_directory:
        folder_path = download_chapter(manga_name, chapter_id, output_directory)
        create_html(folder_path)

        status_label.config(text=f"Download completed. HTML file created at: {folder_path}/index.html", anchor='center')
    else:
        status_label.config(text="Please fill in all the fields.", anchor='center')

root = tk.Tk()
root.title("MangaDex Chapter Downloader")
root.geometry("500x500")

background_image = tk.PhotoImage(file="img/SaintMichaelv2.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

manga_name_label = tk.Label(root, text="Manga Name:")
manga_name_entry = tk.Entry(root, width=30)

chapter_id_label = tk.Label(root, text="Chapter ID:")
chapter_id_entry = tk.Entry(root, width=30)

download_button = tk.Button(root, text="Download Chapter", command=on_download_button_click)

status_label = tk.Label(root, text="")

manga_name_label.place(relx=0.5, rely=0.4, anchor="center")
manga_name_entry.place(relx=0.5, rely=0.45, anchor="center")

chapter_id_label.place(relx=0.5, rely=0.5, anchor="center")
chapter_id_entry.place(relx=0.5, rely=0.55, anchor="center")

download_button.place(relx=0.5, rely=0.6, anchor="center")

status_label.place(relx=0.5, rely=0.7, anchor="center")

root.mainloop()