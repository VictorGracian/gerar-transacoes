from gerar_transacoes.gerador_de_transacoes import abrirSistema
from gerar_transacoes.gerador_de_transacoes import selecionarEmpresa
from gerar_transacoes.gerador_de_transacoes import gerarTransacao
import time


abrirSistema()
time.sleep(10)
selecionarEmpresa()
time.sleep(2)
gerarTransacao()
