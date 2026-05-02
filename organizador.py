import os
import shutil

DIRETORIO_ALVO = r"C:\Users\Usuário\Downloads"

EXTENSOES = {
    'Imagens': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documentos': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Videos': ['.mp4', '.mov', '.avi']
}

def organizar():
    if not os.path.exists(DIRETORIO_ALVO):
        print("Diretório não encontrado.")
        return

    total = 0

    for arquivo in os.listdir(DIRETORIO_ALVO):
        caminho_arquivo = os.path.join(DIRETORIO_ALVO, arquivo)

        if os.path.isdir(caminho_arquivo):
            continue

        extensao = os.path.splitext(arquivo)[1].lower()

        for pasta, extensoes in EXTENSOES.items():
            if extensao in extensoes:
                pasta_destino = os.path.join(DIRETORIO_ALVO, pasta)
                os.makedirs(pasta_destino, exist_ok=True)

                shutil.move(caminho_arquivo, os.path.join(pasta_destino, arquivo))
                print(f"{arquivo} → {pasta}")
                total += 1
                break

    print(f"\nTotal de arquivos organizados: {total}")

if __name__ == "__main__":
    organizar()