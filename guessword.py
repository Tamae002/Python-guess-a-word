from worddataset import words
import random

def get_rand_words():
    valid_words = [letter.upper() for letter in random.choice(words)]
    return valid_words

def hangman():
    word = get_rand_words()
    private_word, guessed_word = ['-' for i in word], []
    placeholder = ''
    word_len, health, word_join = len(word), 6, ''.join(word)
    print('#'*50)
    print('WELCOME TO GUESS WORD!'.center(50, ' '))
    print('Guess the correct letter one by one!'.center(50, ' '))
    print('#'*50)
    while word_len > 0:
        if health == 0:
            print(f'\n You Lose! \n The Word is {word_join}\n'.center(50, ' '))
            break
        print(' '.join(private_word))
        letter = input(f'Guess a letter from the word above: {placeholder} ').upper().strip()
        guessed_word.append(letter)
        duplication_handling = list(set(guessed_word))
        placeholder = ' '.join(duplication_handling)
        try:
            i = word.index(letter)
            b = 0
            for a in word:
                if a == letter:
                    private_word[b] = word[b]
                b += 1
            if guessed_word.count(letter) < 2:
                word_len -= word.count(letter)
            else:
                print('Exception! = Letter already used!')
        except:
            health -= 1
            print(f'(Health = {health}/6)')
            print('Letter not found :(')
            continue
    else:
        print('#'*50)
        print('CONGRATULATION!'.center(50, ' '),'\n',' '.join(private_word).center(50, ' '))
        print('You Guess the word!'.center(50, ' '))
        print('#'*50)
hangman()
    