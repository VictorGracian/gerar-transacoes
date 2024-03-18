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
    time.sleep(5)
    robo.click(x=397, y=338)
    robo.write("victor.graciano") #nome usuario
    robo.click(x=439, y=393)
    robo.write("vic1vini2gui3") #senha
    robo.click(x=462, y=446) # clicando em entrar
    print("sistema aberto")

def selecionarEmpresa():
    #Selecionando empresa
    robo.write("16")
    robo.press("enter")
    time.sleep(1)
    
    #Selecionando filial
    robo.write("1")
    robo.press("enter")
    time.sleep(1)
    
    #Selecionando periodo
    robo.write("01/01/2020")
    robo.press("enter")
    time.sleep(1)
    robo.write("31/12/2100")
    
    #Finalizando
    robo.press("enter")
    robo.press("enter")
    print("empresa selecionada")
    
def gerarTransacao():
    #Escolhendo a rotina
    robo.click(x=378, y=31)
    time.sleep(1)
    robo.click(x=477, y=409)
    time.sleep(1)
    robo.click(x=806, y=419)
    time.sleep(1)
    
    #Configuração
    robo.doubleClick(x=287, y=134)
    time.sleep(1)
    robo.write("01/01/2020")
    time.sleep(1)
    robo.press("enter")
    time.sleep(1)
    robo.write("31/12/2100")
    time.sleep(1)
    
    #execução
    robo.click(x=305, y=99)
    time.sleep(1)
    robo.click(x=890, y=403)






time.sleep(3)
robo.position()


