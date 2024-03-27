# Importar módulos
from palavras import palavras
import random

def selecionar_palavra():
  palavra = random.choice(palavras)
  return palavra.upper()


def jogar(palavra):

  palavra_a_completar = "_" * len(palavra) 
  advinhou = False
  letras_utilizadas = []
  palavras_utilizadas = []
  tentativas = 6


  print("Vamos jogar!")
  print(exibir_forca(tentativas))
  print("Esta é a palavra: %s" % palavra_a_completar)

  while not advinhou and tentativas > 0:

    tentativa = input("Digite uma palavra ou letra para continuar: ").upper()


    if len(tentativa) == 1 and tentativa.isalpha():

      if tentativa in letras_utilizadas:
        print("Você já utilizou esta letra antes: %s" % tentativa)

      elif tentativa not in palavra:
        print("A letra %s não está na palavra" % tentativa)
        tentativas -= 1
        letras_utilizadas.append(tentativa)

      else:
        print("Você acertou! A letra %s está na palavra" % tentativa)
        letras_utilizadas.append(tentativa)

        palavra_lista = list(palavra_a_completar)


        indices = [i for i, letra in enumerate(palavra) if letra == tentativa]
        for indice in indices:
          palavra_lista[indice] = tentativa

        palavra_a_completar = "".join(palavra_lista)

        if "_" not in palavra_a_completar:
          advinhou = True

    elif len(tentativa) == len(palavra) and tentativa.isalpha():

      if tentativa in palavras_utilizadas:
        print("Você já utilizou está palavra %s" % tentativa)
  
      elif tentativa != palavra:
        print("A palavra %s está incorreta!" % tentativa)
        tentativas -= 1
        palavras_utilizadas.append(tentativa)

      else:
        advinhou = True
        palavra_a_completar = palavra


    else:
      print("Tentativa inválida, tente novamente!")


    print(exibir_forca(tentativas))
    print(palavra_a_completar)


  if advinhou:
    print("Parabéns! Você acertou a palavra")
  else:
    print("Acabaram as tentivas, a palavra era: %s" % palavra)


def exibir_forca(tentativas):
  estagios = [  
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / \\
                  -
              """,
           
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / 
                  -
              """,
           
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |      
                  -
              """,
      
              """
                  --------
                  |      |
                  |      O
                  |     \\|
                  |      |
                  |     
                  -
              """,

              """
                  --------
                  |      |
                  |      O
                  |      |
                  |      |
                  |     
                  -
              """,

              """
                  --------
                  |      |
                  |      O
                  |    
                  |      
                  |     
                  -
              """,

              """
                  --------
                  |      |
                  |      
                  |    
                  |      
                  |     
                  -
              """
  ]

  return estagios[tentativas]


def iniciar():
  palavra = selecionar_palavra()
  jogar(palavra)

  while input("Jogar novamente? (S/N)").upper() == "S":
    palavra = selecionar_palavra()
    jogar(palavra)

iniciar()