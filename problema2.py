palavra = ''

while( len(palavra) < 9 or len(palavra) > 1000):
    palavra = input('Digite a palavra: ')
    tempo = 0
    tempo_tecla_pressionada = 0.00


    for p in palavra:
        tempo_tecla_pressionada  += 0.01
        tempo = tempo_tecla_pressionada





print(f'Tempo necessário para escrever a palavra {palavra} foi de: {round(tempo, 2)}')