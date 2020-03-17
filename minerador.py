#Imports necessários do bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import urllib.parse
import json

def executar():
  #Selecionar o site
  url = 'https://hipsters.jobs/jobs/?l=Brasilia%20-%20Federal%20District%2C%20Brazil&p=1'
  soup = BeautifulSoup(urlopen(url),"html.parser")
  time.sleep(15)
  print("\n****************************\n")
  

  #Quantidade de vagas disponíveis
  quantidade = soup.find("h1", class_='search-results__title col-sm-offset-3 col-xs-offset-0').get_text().strip()
  print(quantidade)
  quantidade = quantidade.split()
  quantidade = ''.join(quantidade[0:1])
  quantidade = int(quantidade)

  #quantidade de vagas da página principal
  vagas = 0
  links = []
  for item in soup.select(".listing-item__title"):
    link = item.a.get('href')
    links.append(link)
    vagas += 1

  #Verifica se há vagas escondidas e as captura
  if quantidade != vagas:
    for i in range(2,50):
      url = 'https://hipsters.jobs/jobs/?l=Brasilia%20-%20Federal%20District%2C%20Brazil&p={}'.format(str(i))
      print(url)
      time.sleep(15)
      soup = BeautifulSoup(urlopen(url),"html.parser")
      for item in soup.select(".listing-item__title"):
        link2 = item.a.get('href')
        if link2 not in links:
          links.append(link2)
          vagas += 1
          if vagas == quantidade:
            print("{} vagas capturadas".format(vagas))
            break 
      break

  titulos = []
  salarios = []
  tags = []
  datas = []
  empresas = []
  locais = []
  descricoes = []
  protocolo = 'https:'
  cont = 1

  #Entra em cada Vaga individualmente e pega as informações 
  for i in links:
    time.sleep(60)
    url = i
    url = protocolo + urllib.parse.quote(url[len(protocolo):])
    print(cont)
    cont += 1
    print(url)
    soup = BeautifulSoup(urlopen(url),"html.parser")
    titulos.append(soup.find("h1", class_='details-header__title').get_text().strip()) 
    empresas.append(soup.find("li", class_='listing-item__info--item listing-item__info--item-company').get_text().strip())
    locais.append(soup.find("li", class_='listing-item__info--item listing-item__info--item-location').get_text().strip())
    datas.append(soup.find("li", class_='listing-item__info--item listing-item__info--item-date').get_text().strip())
    tag = soup.find_all("span", class_="job-type__value")
    lista_de_tags = []
    #Cria um lista de tags para cada vaga
    for i in tag:
      i = i.get_text().strip()
      lista_de_tags.append(i)
      tags.append(lista_de_tags)
    #Pega o salario e a descrição e depois os separa, verificando se o salario foi informado ou não
    descricao_e_salario = soup.find_all('div',class_="details-body__content content-text")
    descricoes.append(descricao_e_salario[0].get_text().strip())
    if len(descricao_e_salario) == 2:
      salarios.append(descricao_e_salario[1].get_text().strip())
    else:
      salarios.append('O salário não foi informado na vaga')

  #Retira o código do titulo da vaga
  for i in titulos:
    if (i.find(':') > -1):
      i = i [:len(i)-12]

  #Cria o dicionário
  lista_de_vagas = []
  for i in range(0, len(titulos)):
    vaga = {
          links[i]: (datas[i],
                    titulos[i],
                    locais[i],
                    empresas[i],
                    descricoes[i],
                    salarios[i],
                    tags[i]
                        )
          }
    lista_de_vagas.append(vaga)

  #Cria arquivo Json
  nome_arquivo = "vagas_json.json"
  vagas_json = json.dumps(lista_de_vagas, ensure_ascii=False, indent = 2)
  arquivo = open(nome_arquivo,'w')
  arquivo.write(vagas_json)
  arquivo.close()

if(__name__ == "__main__"):
	executar()


    

     


