import subprocess

def abrir_chrome():
    caminho_chrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    
    links = ["file:///C:/Users/CONTAC/Documents/Digital.html"]
    try:
        subprocess.Popen([caminho_chrome,"--start-fullscreen", *links])
        print("Google Chrome foi aberto com sucesso!")
    except FileNotFoundError:
        print("Erro: Caminho do Chrome não encontrado.")

if __name__ == "__main__":
    abrir_chrome()
