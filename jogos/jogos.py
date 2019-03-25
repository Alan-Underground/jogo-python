import forca
import adivinhacao

def escolhe_jogo():
    print("********************************")
    print("*******Escolha o seu jogo*******")
    print("********************************")

    print("(1) Forca  (2) Adivinhacao")

    jogo= int(input("Digite o valor"))

    if (jogo==1):
        print("jogo da forca \o/")
        forca.jogar_forca()

    elif(jogo==2):
        print("jogando Adivinhação")
        adivinhacao.jogar_adivinhacao()

if(__name__ == "__main__"):
    escolhe_jogo()