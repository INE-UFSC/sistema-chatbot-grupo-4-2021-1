#encoding: utf-8
from Bots.BotAgiota import BotAgiota
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotCansado import BotCansado

###construa a lista de bots disponíveis aqui
lista_bots = [BotCansado("Mai"), BotAgiota("Hulk")]

sys = scb.SistemaChatBot("Bots Irados", lista_bots)
sys.inicio()
