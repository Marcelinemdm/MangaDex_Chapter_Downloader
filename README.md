## README

### MangaDex Chapter Image Downloader (Script 1)

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

### MangaDex Chapter Image Downloader (Script 2)

This Python script allows you to download the images for a specific manga chapter from Mangadex. The script prompts the user to input the manga name and chapter ID, and it creates a folder structure to store the downloaded images. Additionally, it generates an HTML file with image tags referencing the downloaded images.

#### Instructions:

1. **Requirements:**
   - Python
   - Requests library (install using `pip install requests`)

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

---

## README

### Baixador de Imagens de Capítulo no MangaDex (Script 1)

Este script em Python permite obter os URLs de imagem para um capítulo específico de manga no Mangadex sem baixar as imagens. O script solicita ao usuário que insira o nome do manga e o ID do capítulo e, em seguida, gera um arquivo HTML contendo tags de imagem com os URLs correspondentes. O arquivo HTML é estilizado usando o código CSS fornecido.

#### Instruções:

1. **Requisitos:**
   - Python
   - Biblioteca Requests (instale usando `pip install requests`)

2. **Como Usar:**
   - Execute o script.
   - Insira o nome do manga e o ID do capítulo quando solicitado.
   - O script gerará um arquivo HTML no diretório de saída especificado (`projeto` neste exemplo).

3. **Observações:**
   - Certifique-se de personalizar o código CSS de acordo com suas preferências de estilo.
   - Ajuste a variável `output_directory` para o caminho de saída desejado.
   - **Importante:** Este script pode não funcionar em algumas situações devido às políticas da Mangadex. No entanto, a URL utilizada no atributo `src` do HTML gerado contém as informações do capítulo.

### Baixador de Imagens de Capítulo no MangaDex (Script 2)

Este script em Python permite baixar as imagens de um capítulo específico de manga no Mangadex. O script solicita ao usuário que insira o nome do manga e o ID do capítulo, cria uma estrutura de pastas para armazenar as imagens baixadas e gera um arquivo HTML com tags de imagem referenciando as imagens baixadas.

#### Instruções:

1. **Requisitos:**
   - Python
   - Biblioteca Requests (instale usando `pip install requests`)

2. **Como Usar:**
   - Execute o script.
   - Insira o nome do manga e o ID do capítulo quando solicitado.
   - O script baixará as imagens do capítulo em uma estrutura de pastas e criará um arquivo HTML referenciando essas imagens.
   - A estrutura de pastas é criada no diretório de saída especificado (`projeto` neste exemplo).

3. **Observações:**
   - Certifique-se de personalizar o código CSS de acordo com suas preferências de estilo.
   - Ajuste a variável `output_directory` para o caminho de saída desejado.

**Nota Importante:**
O HTML e CSS da página `/home` não foram testados e provavelmente precisarão ser ajustados por quem for utilizar.