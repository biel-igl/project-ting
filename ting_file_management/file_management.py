import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido")
    try:
        with open(path_file, "r") as text:
            lines = text.readlines()
            for i in range(len(lines)):
                lines[i] = lines[i].rstrip()
            return lines

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
