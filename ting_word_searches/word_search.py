def exists_word(word, instance):
    ocorrencias = []
    for item in instance._data:
        arquivo = item["nome_do_arquivo"]
        lines_find = []
        for index, line in enumerate(item["linhas_do_arquivo"], start=1):
            if word.lower() in line.lower():
                lines_find.append({"linha": index})
        if lines_find:
            ocorrencias.append({
                "palavra": word,
                "arquivo": arquivo,
                "ocorrencias": lines_find
            })
    return ocorrencias


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
