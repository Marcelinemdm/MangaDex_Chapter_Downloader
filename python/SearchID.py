import requests
import tkinter as tk
from tkinter import filedialog
import pyperclip

def get_manga_ids(title):
    base_url = "https://api.mangadex.org"
    r = requests.get(f"{base_url}/manga", params={"title": title})
    manga_ids = [manga["id"] for manga in r.json()["data"]]
    return manga_ids

def on_search_button_click():
    manga_title = manga_title_entry.get()
    if manga_title:
        manga_ids = get_manga_ids(manga_title)
        result_label.config(text=f"Manga IDs: {', '.join(map(str, manga_ids))}")
        copy_button.config(state="normal")
    else:
        result_label.config(text="Please enter a manga title.")
        copy_button.config(state="disabled")

def on_copy_button_click():
    manga_ids_text = result_label.cget("text")
    manga_ids = manga_ids_text.split(":")[1].strip()
    pyperclip.copy(manga_ids)
    copy_button.config(text="Copied!", state="disabled")

root = tk.Tk()
root.title("MangaDex Manga ID Finder")
root.geometry("500x500")

canvas = tk.Canvas(root)
canvas.pack(fill="both", expand=True)

background_image = tk.PhotoImage(file="img/SaintMichaelv2.png")
canvas.create_image(0, 0, anchor="nw", image=background_image)

manga_title_label = tk.Label(canvas, text="Manga Title:", bg="white")
manga_title_entry = tk.Entry(canvas)

search_button = tk.Button(canvas, text="Search Manga IDs", command=on_search_button_click, bg="#3498db", fg="white")
copy_button = tk.Button(canvas, text="Copy IDs", command=on_copy_button_click, bg="#2ecc71", fg="white", state="disabled")

result_label = tk.Label(canvas, text="", bg="white")

canvas.create_window(250, 50, window=manga_title_label)
canvas.create_window(250, 80, window=manga_title_entry)
canvas.create_window(250, 120, window=search_button)
canvas.create_window(250, 160, window=copy_button)
canvas.create_window(250, 220, window=result_label)

root.mainloop()
