from __future__ import print_function 
word = 'earring'
lives = 6
spaces = [('_ ') * len(word)]
def initialize():
    global word
    print (''.join(spaces))
    print('Lives = 6')
    getLetter()
def getLetter():
    global letter
    letter = raw_input('Your guess: ')
    #check()
    if letter not in word:
        print('Lives = ', (lives-1))
def won ():
    if ('_') in spaces:
        getletter()
    else:
        print('You have guessed the word! Congradulations, you have won!')
        
def main():
    initialize()
    
main()