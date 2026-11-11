import pdfplumber

with pdfplumber.open("relatorio.pdf") as pdf:
  primeira_pagina = pdf.pages[0]
  tabela = primeira_pagina.extract_table()

#print(tabela[1]) segunda linha da tabela

tabela.pop(0)
#print(tabela[5][0]) 

tabela = [
    row for row in tabela 
    if row[0] and not (row[6].startswith("Folga") or row[6].startswith("Feriado") or row[6].startswith("Ponto Fac"))
]     

entradas = []
saidas = []
data_faltas = []

for linha in tabela:
  
    try:
        hora_entrada, hora_saida = linha[1].split()
        entradas.append(hora_entrada)
        saidas.append(hora_saida)
    except ValueError:
       falta = linha[1]
       data_faltas.append(linha[0])
       #print(f"{linha[0]} - Ponto faltante identificado na")
       #print("Ponto batido no dia: ",falta)

#print("Entradas: ", entradas)
#print("Saídas: ", saidas)

print("Datas das faltas:",data_faltas)

n = 0
index_faltas = []
hora_falta = [ ]

for linha in tabela:
    linha.append(n)
    #print(linha)
    
    for i in range(len(data_faltas)):
        if data_faltas[i] == linha[0]:
            hora_falta.append(linha[1])
            index_faltas.append(n)
    n += 1
    print(linha)

dicionario = dict(zip(index_faltas,hora_falta))

for h in hora_falta:
    hora,min = h.split(':')
    #if hora == '07':


print("Indexes dos dias com ponto faltante:",index_faltas)
print("Hora registrada no dia com ponto faltante:",hora_falta)


""" 
['Sex - 06/11', '07:25 13:35', '06:00', '06:10', '06:00', '', 'Extras 00:10;']
['Sáb - 07/11', '', '', '', '', '', 'Folga;']
['Dom - 08/11', '', '', '', '', '', 'Folga;']
['Seg - 09/11', '07:28 13:37', '06:00', '06:09', '06:00', '', 'Extras 00:09;']
['Ter - 10/11', '07:31', '', '', '06:00', '', 'Atraso 00:01;']
['', None, None, None, None, None, None] """


""" O que é preciso para preencher a ocorrência?
Data da falta
hora (final ou inicial) """