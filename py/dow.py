import os
import requests

chapter_id = '45f7fa47-265e-4a16-9610-fbd3def4cfdf'

folder_path = f"Mangadex/{chapter_id}"
os.makedirs(folder_path, exist_ok=True)

chapter_info = requests.get(f"https://api.mangadex.org/at-home/server/{chapter_id}").json()
host = chapter_info['baseUrl']
chapter_hash = chapter_info['chapter']['hash']
data = chapter_info['chapter']['data']

for page in data:
    r = requests.get(f"{host}/data/{chapter_hash}/{page}")

    with open(f"{folder_path}/{page}", mode="wb") as f:
        f.write(r.content)

print(f"Downloaded {len(data)} pages.")
