# Convertidor masivo de ebooks de epub a mobi con Calibre

## lote-ebooks.py

Es un script python para convertit todos los libros de una carpeta de epub a mobi usando Calibre.
Necesitáis tener instalado Calibre:

En Debian / Ubuntu / Raspbian sería:

`sudo apt-get install calibre`

Para para evitar problemas con gráficos se debería instalar:

`sudo apt-get install xvfb`

Para luego poder usarlo con `ebook-convert` de la siguiete forma `xvfb-run ebook-convert libro.epub libro.mobi`


El scritp original es de **kovidgoyal** y fue copiado del foro de **mobileread**  http://www.mobileread.com/forums/showthread.php?t=179686
