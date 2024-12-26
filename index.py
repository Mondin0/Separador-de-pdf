import PyPDF2
import os
import zipfile
import re

def dividir_pdf_por_marcadores(pdf_path):
    # Abrir el archivo PDF
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        marcadores = pdf_reader.outline  # Obtener marcadores (outline)

        # Crear un directorio para almacenar los PDFs divididos
        output_dir = 'pdf_divididos'
        os.makedirs(output_dir, exist_ok=True)

        # Filtrar solo los marcadores principales (ignorar sub-marcadores)
        marcadores_principales = [
            marcador for marcador in marcadores if isinstance(marcador, PyPDF2.generic.Destination)
        ]

        # Obtener las páginas de inicio y fin para cada marcador
        for i, marcador in enumerate(marcadores_principales):
            start_page = pdf_reader.get_destination_page_number(marcador)

            # Determinar la página final
            if i + 1 < len(marcadores_principales):
                end_page = pdf_reader.get_destination_page_number(marcadores_principales[i + 1]) - 1
            else:
                end_page = len(pdf_reader.pages) - 1  # Última página si no hay más marcadores

            # Crear un nuevo archivo PDF
            pdf_writer = PyPDF2.PdfWriter()

            # Agregar las páginas al nuevo PDF desde start_page hasta end_page (inclusive)
            for page in range(start_page, end_page + 1):
                pdf_writer.add_page(pdf_reader.pages[page])

            # Usar el texto del marcador como nombre del archivo (limpiarlo de caracteres no válidos)
            marcador_texto = str(marcador.title).strip()
            marcador_texto = re.sub(r'[<>:"/\\|?*]', '_', marcador_texto)  # Reemplazar caracteres inválidos

            output_filename = os.path.join(output_dir, f'{marcador_texto}.pdf')
            with open(output_filename, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)

    return output_dir

def comprimir_pdfs(output_dir):
    zip_filename = 'pdfs_divididos.zip'
    with zipfile.ZipFile(zip_filename, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zipf:
        for root, _, files in os.walk(output_dir):
            for file in files:
                zipf.write(os.path.join(root, file), file)
    return zip_filename

# Ruta del archivo PDF original
pdf_path = 'archivo.pdf'

# Dividir el PDF y obtener el directorio de salida
output_dir = dividir_pdf_por_marcadores(pdf_path)

# Comprimir los archivos PDF en un ZIP
zip_filename = comprimir_pdfs(output_dir)

print(f'Los archivos PDF han sido divididos en {output_dir} y comprimidos en {zip_filename}.')
