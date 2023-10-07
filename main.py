import hashlib
import csv


def calcular_md5(texto):
    return hashlib.md5(texto.encode('utf-8')).hexdigest()


def calcular_sha256(texto):
    return hashlib.sha256(texto.encode('utf-8')).hexdigest()


def validar_hash(texto, hash_fornecido):
    md5_calculado = calcular_md5(texto)
    sha256_calculado = calcular_sha256(texto)

    if md5_calculado == hash_fornecido:
        return "MD5", True
    elif sha256_calculado == hash_fornecido:
        return "SHA-256", True
    else:
        return None, False


if __name__ == "__main__":
    with open('frases.csv', 'r') as arquivo_csv:
        arquivo_csv = csv.DictReader(arquivo_csv)
        for linha in arquivo_csv:
            frase = linha['frase']
            md5_hash = linha['md5_hash']
            sha256_hash = linha['sha256_hash']

            print(f"\n{frase}")

            tipo, valido = validar_hash(frase, md5_hash)
            if valido:
                print(f"O hash fornecido é um hash {tipo} válido.")
            else:
                print(f"O hash MD5 fornecido não é válido.")
                print(f"Hash MD5 correto: {calcular_md5(frase)}")

            tipo, valido = validar_hash(frase, sha256_hash)
            if valido:
                print(f"O hash fornecido é um hash {tipo} válido.")
            else:
                print(f"O hash SHA-256 fornecido não é válido.")
                print(f"Hash SHA-256 correto: {calcular_sha256(frase)}")
