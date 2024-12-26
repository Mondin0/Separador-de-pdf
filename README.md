## Script para cortar PDF's por marcadores

Solicitado para cortar archivos pdf, donde en un solo pdf vienen muchos registros juntos separados por marcadores.
La primer pagina del marcador es la primera que contiene informacion, y la ultima es la anterior a la "Pagina 0" del siguiente marcador.
Se pueden separar libros por capítulo por ejemplo

## Descripción del Código

1. **Dividir PDF por Marcadores**:

   - Utiliza `PyPDF2.PdfReader` para leer el PDF y sus marcadores.
   - Filtra solo los marcadores principales, ignorando sub-marcadores.
   - Crea un archivo PDF por cada marcador, desde la página de inicio hasta la anterior al siguiente marcador.

2. **Nombres de Archivos**:

   - Los archivos resultantes llevan el nombre del marcador como título.
   - Se reemplazan caracteres problemáticos (`/` y `\\`) para evitar errores.

3. **Compresión en ZIP**:
   - Todos los archivos generados se comprimen en un archivo ZIP llamado `pdfs_divididos.zip`.

## Salida

- Los PDFs generados se guardan en una carpeta `pdf_divididos`.
- El archivo ZIP resultante se guarda en el directorio de trabajo actual.

## Ejecución

Para instalar las dependencias desde el archivo requirements.txt utilizando pip, ejecuta:

```bash
pip install -r requirements.txt
```

Si se tiene conda en una maquina, para usar el mismo entorno con las mismas librerias usar

```bash
conda env create -f environment.yml
conda activate entornoeditarpdf
```

Asegúrate de colocar el archivo PDF que deseas dividir en el mismo directorio que el script y modifica el nombre del archivo a "archivo.pdf".

```bash
python index.py
```

Para eliminar el entorno despues del uso ejecutar:

```bash
conda env remove --name entornoeditarpdf
```
