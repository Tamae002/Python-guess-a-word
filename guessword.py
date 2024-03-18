from worddataset import words # import data words from worddataset file
import random


def get_rand_words():
    valid_words = [letter.upper() for letter in random.choice(words)]
    return valid_words
# generating a list of every letter in a random word that's chosen

def guessword():
    word = get_rand_words()
    private_word, guessed_word = ['-' for i in word], []
    placeholder = ''
    word_len, health, word_join = len(word), 6, ''.join(word)
    print('#'*50)
    print('WELCOME TO GUESS WORD!'.center(50, ' '))
    print('Guess the correct letter one by one!'.center(50, ' '))
    print('#'*50)
    while word_len > 0: # while all the letters in the word aren't guessed keep looping
        if health == 0: # break the loop if input guessed wrong 6 times
            print(f'\n You Lose! \n The Word is {word_join}\n'.center(50, ' '))
            break
        print(' '.join(private_word))
        letter = input(f'Guess a letter from the word above: {placeholder} ').upper().strip()
        guessed_word.append(letter)
        duplication_handling = list(set(guessed_word))
        placeholder = ' '.join(duplication_handling)
        try:
            word.index(letter)
            b = 0
            for a in word: # check one by one if the input letter matches with the word
                if a == letter:
                    private_word[b] = word[b] #change values of private_word with the correct letter with index b
                b += 1
            if guessed_word.count(letter) < 2: #duplication handling
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
guessword()
    
