import minerador
import bot

def escolher():
  
  print("\nSelecione a função a ser realizada\n")
  print("(1) Minerar vagas Hipsters Jobs \n(2) Enviar mensagens pelo Bot do Telegram \n")
  escolha = int(input())

  if escolha == 1:
      print('Executando Minerador...')
      minerador.executar()

  if escolha == 2:
      print('Executando Bot Telegram...')
      bot.executar()

if(__name__ == "__main__"):
	escolher()
