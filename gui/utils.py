def validarNumero(texto):
    if texto == "":
        return True
    return texto.isdigit() and len(texto) <= 4
