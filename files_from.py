# funcion para extraer la lista de ficheros de una carpeta separada por espacios con el path completo
# name: files_from.py
# call as:  python3 files_from.py 'path'

import sys
import glob

def files_from(path):
    files = glob.glob(path)
    return ' '.join(files)

if __name__ == '__main__':
    path = sys.argv[1]
    print(files_from(path))