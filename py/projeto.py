import os
import requests

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

# Get input from the user
manga_name = input("Nome do manga: ")
chapter_id = input("ID do capítulo: ")
output_directory = r"projeto"

# Download the chapter and get the folder_path
folder_path = download_chapter(manga_name, chapter_id, output_directory)

# Generate HTML file with images and CSS
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

ul {
  list-style: none;
  display: flex;
  gap: 20px;
  margin: 0;
  padding: 0;
}

ul li a {
  text-decoration: none;
  color: #ffffff;
}

main {
  padding: 10px;
}

main.bg-blueglobal1900 {
  background: linear-gradient(to right, #101d42, #0d1317);
  width: 1050px;
  margin: 15px auto;
  border-radius: 25px;
}

.container {
  max-width: 800px;
  margin: 0 auto;
}

.container p {
  font-size: 21px;
  font-weight: bold;
  margin-bottom: 20px;
}

.obra {
  display: flex;
  gap: 20px;
}

.obra img {
  width: 250px;
  height: auto;
}

.obra > div {
  flex-grow: 1;
}

.visualizacoes,
.autor,
.artista,
.genero,
.status {
  font-size: 18px;
  margin-bottom: 10px;
}

.sinopse {
  margin-top: 20px;
}

.capitulos {
  overflow-y: auto;
  max-height: 150px;
  max-width: 800px;
  display: flex;
  flex-wrap: wrap;
}

.capitulo-item {
  width: 210px;
  height: 31px;
  margin: 4px;
  padding: 4px;
  background-color: #374151;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 25px;
}

.capitulos p {
  font-size: 16px;
  color: white;
  margin: 0;
}

footer {
  padding: 10px;
  text-align: center;
  color: white;
  position: fixed;
  bottom: 0;
  width: 100%;
}
'''

# Generate HTML file with images and CSS
html_base = f'''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TQ = tenho queijo</title>
  <link rel="stylesheet" href="style.css">
  <link rel="shortcut icon" href="/logo.png" type="image/x-icon">
  <style>
    {css_code}
  </style>
</head>
<body>
  <header>
    <img src="/logo.png" alt="logo">
    <ul>
      <li>
        <a href="/">inicio</a>
      </li>
      <li>
        <a href="/projetos +18/">+18</a>
      </li>
      <li>
        <a href="https://discord.gg/ywfRCz52">discord</a>
      </li>
      <li class="search">
        <img src="/search.svg" alt="search">
      </li>
    </ul>
  </header>
  <main class="bg-blueglobal1900">
'''

# Add image tags to the HTML
for page in os.listdir(folder_path):
    html_base += f'''
      <img src="{page}" alt="page">
    '''

# Add the remaining HTML
html_base += '''
  </main>
  <footer>
    <p>© 2023 - Todos os direitos reservados.</p>
  </footer>
</body>
</html>
'''

# Write the HTML to a file
with open(f"{folder_path}/index.html", mode="w", encoding="utf-8") as html_file:
    html_file.write(html_base)

print(f"HTML file created: {folder_path}/index.html")