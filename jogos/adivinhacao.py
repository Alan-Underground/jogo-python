import random

def jogar_adivinhacao():
    print("********************************")
    print("bem vindo ao jogo de adivinhacao")
    print("********************************")

    numero_secreto = round(random.randrange(1,101))
    numero_de_tentativas = 3
    rodada = 1
    pontos = 1000


    print("Qual o o nível de dificuldade que você quer?")
    print("(1)Baixo (2)Médio (3)Dificil")

    nivel = int(input("Digite o nível desejado: "))

    if (nivel ==1 ):
        numero_de_tentativas = 20
    elif(nivel ==2):
        numero_de_tentativas = 10
    else:
        numero_de_tentativas = 5


    for rodada in range (1, numero_de_tentativas+1):

        print ("esta é a rodada {} de {}".format(rodada, numero_de_tentativas) )
        chute_str = input("Digite um número entre 1 e 100")
        print("você digitou", chute_str)
        chute_int = int(chute_str)

        if (chute_int<1 or chute_int>100):
            print("você digitou um valor abaixo de 1, por favor inserir valor entre 1 e 100")
            continue


        acertou     = chute_int == numero_secreto
        chute_maior = chute_int > numero_secreto
        chute_menor = chute_int < numero_secreto




        if (acertou):
            print("voce acertou e fez{} pontos".format(pontos))
            break
        else:
            if(chute_maior):
                print("Você errou , seu chute foi maior que o número secreto")
            elif(chute_menor):
                print("Você errou , seu chute foi menor que o número secreto")
        pontos_perdidos = abs(numero_secreto-chute_int)
        pontos = pontos - pontos_perdidos


    print("Fim do Jogo")



if (__name__ =="__main__"):
    jogar_adivinhacao()

