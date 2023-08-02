from autocorrect import Speller


def corretor(frase, idioma):
    red_color = "\033[31m"
    green_color = "\033[32m"
    reset_color = "\033[0m"

    frase = "teste c0m letra 0"
    idioma = 'pt'

    spell = Speller(lang=str(idioma))
    misspelled = frase.split()

    for word in misspelled:
        if word != (spell(word)):
            print("Você quer dizer " + green_color + spell(word) + reset_color + 
                  " ao invés de " + red_color + word + reset_color + "?")
        else:
            print("A palavra " + green_color + word + reset_color + " está correta!")
