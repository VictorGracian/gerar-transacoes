# Abrir questor na contabilidade
# Fazer Login
# Selecionar empresa
# Gerar transação
# Trocar empresa
# Gerar Transação

import pyautogui as robo
import time

def abrirSistema():
    #abrindo o sistema
    robo.press("win")
    time.sleep(2)
    robo.write("nctb")
    time.sleep(2)
    robo.press("enter")

    #fazendo login
    time.sleep(2)
    robo.click(x=397, y=338)
    robo.write("victor.graciano") #nome usuario
    robo.click(x=439, y=393)
    robo.write("vic1vini2gui3") #senha
    robo.click(x=462, y=446) # clicando em entrar
    print("sistema aberto")






time.sleep(3)
robo.position()