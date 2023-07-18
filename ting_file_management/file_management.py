import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido")
    try:
        with open(path_file, "r") as text:
            lines = [line.rstrip() for line in text]
        return lines

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
