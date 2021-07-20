#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotCansado import BotCansado
from Bots.BotAgiota import BotAgiota
from Bots.BotSulMatogrossense import BotSulMatogrossense

###construa a lista de bots disponíveis aqui
lista_bots = [BotCansado("Mai"), BotAgiota("Hulk"), BotSulMatogrossense("Maria")]

sys = scb.SistemaChatBot("Bots Irados", lista_bots)
sys.inicio()
