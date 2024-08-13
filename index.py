import pyautogui
import time, os

# Caminho para a imagem do botão
button_image = 'botao.png'

# Tempo máximo de execução em segundos (10 minutos)
max_time = 10 * 60

# Marca o tempo de início
start_time = time.time()

print("Iniciando a procura pelo botão...")

while True:
    try:
        # Captura a tela e procura pela imagem do botão
        button_location = pyautogui.locateOnScreen(button_image, confidence=0.7)
        
        if button_location:
            # Obtém o centro do botão
            button_center = pyautogui.center(button_location)
            # Move o mouse para o centro do botão e clica
            print("Movendo o mouse para o centro do botão e clicando...")
            pyautogui.click(button_center)
            print("Botão clicado!")
            break
        else:
            print("Botão não encontrado. Tentando novamente...")
        
        # Verifica se o tempo máximo foi atingido
        if time.time() - start_time > max_time:
            print("Erro: Tempo máximo de 10 minutos atingido sem encontrar o botão.")
            break
        
        # Aguarda um pouco antes de verificar novamente
        time.sleep(1)
    except pyautogui.ImageNotFoundException:
        os.system('cls')
        print("Procurando partida")
    except Exception as e:
        print(f"Erro ao localizar o botão: {e}")
        break

print("Script finalizado.")
