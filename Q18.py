#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).


print("Vamos calcular o tempo de download do seu aquivo ")
downloadStr = input("Qual o tamanho do aquivo que você pretende baixar (em MB)?")
velocidadeStr = input("Qual a sua velocidade de download (em mbps)?")

download = float(downloadStr)
velocidade = float(velocidadeStr)/8

tempoSeg = download/velocidade
tempoMin = tempoSeg//60
restoSeg = tempoSeg%60

print("o tempo aproximado de download desse aquivo é:", tempoMin,"minutos e",restoSeg,"segundo")
