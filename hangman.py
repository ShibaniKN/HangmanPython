import random

def play_again():
    answer = input('Would you like to play again? yes/no').lower()
    if answer == 'y' or answer =='yes':
        play_game()
    else:
        pass
def get_word():
    words=['dog','cat','python','snake','monkey']
    return random.choice(words)

#print(get_word())

def play_game():
    alphabet='abcdefghijklmnopqrstuvwxyz'
    word = get_word()
    #print(word)
    letters_guessed=[]
    tries=10
    guessed=False

    print('the selected word has ',len(word),' letters')
    print(len(word) * '*')

    while guessed == False and tries>0:
        print('you have '+str(tries)+' tries')
        guess=input('please enter a letter or the entire word to guess').lower()
        #user inputs one letter
        if len(guess) == 1:
            if guess not in alphabet:
                print('you have not entered a letter')
            elif guess in letters_guessed:
                print('you have already guessed that letter before')
            elif guess not in word:
                print('sorry,the letter is not present in word')
                letters_guessed.append(guess)
                tries-=1
            elif guess in word:
                print('Well Done! its there in the word')
                letters_guessed.append(guess)
            else:
                print('no idea why we got this message')

          #user inputs entire word
        elif len(guess)==len(word):
            if guess==word:
                print('congrats!You have guessed the word')
                guessed=True
            else:
                print('oops!this is not the word we were looking for')
                tries-=1

            #user inputs a word of different length
        else:
            print('the length of your guess in not equal to that of the word')

        status=""
        if guessed==False:
            for letter in word:
                if letter in letters_guessed:
                    status+=letter
                else:
                    status+='*'
            print(status)

        if status==word:
            print('Congrats you have guessed the word')
            guessed=True
        elif tries==0:
            print('you have finished all your tries better luck next time')
    play_again()
play_game()