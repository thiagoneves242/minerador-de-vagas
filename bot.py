import telepot
import json
import time

def executar():

  bot = telepot.Bot('949943526:AAHbEhrnUReToKXaNgOIAiZhGuhIv-qdZ5c')
  chat_id = '-1001410055619'

  b = open('ultima_vaga_bot.tmp','r')
  ultima = b.read()
  b.close

  a = open('vagas_json.json','r')
  jsonarq = json.loads(a.read())
  a.close()

  chaves = []
  for i in range(len(jsonarq)):
    chave = list(jsonarq[i].keys())[0]
    chaves.append(chave)
  
  cont = 0
  for i in range(len(chaves)-1),-1,-1:
    vaga = (jsonarq[i][chaves[i]])
    mensagens = "*{}*\n\n*Data de publicação: *{}\n*Local: *{}\n*Empresa: *{}\n\n                   *D E S C R I Ç Ã O*\n\n{}\n\n*Salario: *{}\n\n*Tags da vaga: *{}\n\n{}".format(vaga[1],vaga[0],vaga[2], vaga[3], vaga[4], vaga[5],vaga[6], chaves[i])
      
    
    if chave[i] != ultima:
      bot.sendMessage(chat_id, mensagens, parse_mode='markdown')
      
      cont += 1
      print('{}° vaga de um total de {}'.format(cont, len(chaves)))
      time.sleep(2)

      ultima_vaga_bot = list(jsonarq[i].keys())[0]
      
    else:
      break

  arquivo_tmp = open('ultima_vaga_bot.tmp', 'w')
  arquivo_tmp.write(ultima_vaga_bot)
  arquivo_tmp.close()
    
  print('\nVagas enviadas com sucesso!!!')

if(__name__ == "__main__"):
	executar()

