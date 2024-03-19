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
    time.sleep(1)
    robo.write("nctb")
    time.sleep(2)
    robo.press("enter")

    #fazendo login
    time.sleep(5)
    robo.write("victor.graciano")
    time.sleep(2)
    robo.press("tab")
    time.sleep(2)
    robo.write("vic1vini2gui3")
    time.sleep(2)
    robo.press("tab")
    time.sleep(2)
    robo.press("enter")

def selecionarEmpresa():
    #Selecionando empresa
    robo.write("16")
    robo.press("enter")
    time.sleep(2)
    
    #Selecionando filial
    robo.write("1")
    robo.press("enter")
    time.sleep(2)
    
    #Selecionando periodo
    robo.write("01/01/2020")
    robo.press("enter")
    time.sleep(2)
    robo.write("31/12/2100")
    
    #Finalizando
    robo.press("enter")
    robo.press("enter")

def gerarTransacao():
    #Escolhendo a rotina
    robo.click(x=1030, y=6)
    robo.hotkey("Ctrl","Alt","F1")
    
    #Configurando
    time.sleep(2)
    robo.write("01/01/2020")
    robo.press("tab")
    time.sleep(1)
    robo.write("31/12/2100")
    robo.press("tab")
    robo.press("tab")
    time.sleep(2)
    robo.press("enter")
    print("16 feito")

def repeticao():
    #repetição
    with open(r"C:\Users\victor.graciano\Desktop\i.txt") as arquivo:
        for i in arquivo:
            robo.press("F7")
            time.sleep(1)
            robo.write(i)
            robo.press("enter")
            robo.press("enter")
            robo.press("enter")
            robo.press("enter")
            robo.press("enter")
            time.sleep(1)
            robo.press("F9")
            time.sleep(2)
            robo.press("enter")
            i = i.replace("\n","")
            print(i,"feito")
            time.sleep(15)