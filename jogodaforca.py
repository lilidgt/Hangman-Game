import random

def pick_word():
    words = ['bolo', 'sorvete', 'torta', 'chocolate' 'brigadeiro', 'rosquinha', 'macaron', 'biscoito', 'bolacha', 'granulado', 'geleia', 'beijinho']
    return random.choice(words).lower()

def show_word(word, correct_letters):
    return ''.join([letter if letter in correct_letters else '_' for letter in word])

def hangman_game():
    word = pick_word()
    correct_letters = []
    wrong_letters = []
    remaining_attempts = 6
    won = False

    print("Bem-vindo ao jogo da Forca!")
    print("O tema das palavras é: DOCES!")
    print("A palavra tem", len(word), "letras.")

    while remaining_attempts > 0 and not won:
        print(f"\nPalavra: {show_word(word, correct_letters)}")
        print(f"Letras erradas: {', '.join(wrong_letters)}")
        print(f"Tentativas restantes: {remaining_attempts}")

        guess = input("Digite uma letra: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Por favor, insira apenas uma letra válida.")
            continue

        if guess in correct_letters or guess in wrong_letters:
            print("Você já tentou essa letra.")
            continue

        if guess in word:
            correct_letters.append(guess)
            if set(word) == set(correct_letters):
                won = True
        else:
            wrong_letters.append(guess)
            remaining_attempts -= 1

    if won:
        print(f"\nParabéns! Você adivinhou a palavra '{word}'!")
    else:
        print(f"\nVocê perdeu! A palavra era '{word}'.")

#garante que o bloco de código só seja executado quando o arquivo for rodado diretamente
if __name__ == "__main__":
    hangman_game()
