# História do jogo
# O jogo do número mágico é normalmente uma atividade em uma roda de pessoas onde uma pesso, nomeada como chefe,
#  pensa em um número (ou pega o número de uma tampa) definindo o número mágico da rodada. Após ter o número mágico definido, 
# o chefe fala uma faixa de valores com um número menor e outro número maior que o número mágico. 
# Começa aí o jogo, passando a palavra a cada pessoa da roda falar um número. Se o jogador acertou o número, 
# o chefe informa que o jogador ganhou. Caso o jogador errou o número, o chefe ajusta a faixa de menor e maior com o número informado.
#  Até que alguém advinhe o número ou que a diferença entre o menor e maior número seja de 2.

# Regras iniciais

# A faixa de valores deve ser informada no início
# O número de particitantes deve ser informado no início
# Cada participante tem um nome e deve ser informado no início
# O número mágico deve ser gerado com random.randint no início de cada rodada
# Ganha o jogador quem acertar o número, ou o chefe caso a diferença entre menor e maior seja de 2.
# Regras da rodada

# O chefe define o número mágico e passa a palavra para o jogador inicial
# O chefe define o jogador inicial como o "jogador da vez"
# O jogador da vez informa número
# O chefe informa
# ou a nova faixa de valores
# ou que o jogador foi o vencedor
# ou que o chefe foi vencedor
# Caso o chefe informe a nova faixar de valores
# O chefe define o próximo "jogador da vez"
# Volta ao passo 3, para o "jogador da vez" jogar

import random

menor, maior = map(int, input("Digite o número inicial e o final( o range):").split())
numero = random.randint(menor, maior)
numeros = []
n_participantes = int(input("N de participantes:"))
pessoas = {}

for num in range(menor,maior+1):
    numeros.append(num)

for i in range (n_participantes):
    nome = input(f"Nome {i+1}:")
    chute = int(input(f"Chute de {nome} : "))
    if nome not in pessoas:
        pessoas[nome] = []
    pessoas[nome] = chute

print(pessoas)





