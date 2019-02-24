# coding = utf-8

# Jogo da Forca (Hangman Game)

import random
import os

#Estados da forca

hanging_stages = ['''

>>>>>>>> Hangman <<<<<<<<

 +----+
 |    |
 |
 |
 |
 |
========''', '''

 +----+
 |    |
 |    O
 |
 |
 |
========''', '''

 +----+
 |    |
 |    O
 |    |
 |
 |
========''', '''

 +----+
 |    |
 |    O
 |   /|
 |
 |
========''', '''

 +----+
 |    |
 |    O
 |   /|\ 
 |
 |
========''', '''

 +----+
 |    |
 |    O
 |   /|\ 
 |   /
 |
========''', '''

 +----+
 |    |
 |    O  " OH GOD, YOU LET ME DIE. "
 |   /|\ 
 |   / \ 
 |
========''','''

     " I AM FREE! THANK YOU! "
 \O/  
  |
 / \ ''']

class Hangman:

    def __init__(self, word):
        self.word = word #palavra aleatoria escolhida
        self.right_ans = [] #letras corretas
        self.wrong_ans = [] #letras erradas
        self.hidden_word = list('-'*len(self.word)) #palavra escondida
        self.hang = 0 #estágio do enforcamento

    def checkGuess(self, letter): #checa se palpite está correto
        if letter.upper() in self.right_ans: #checa se letra já não foi usada
            print('\nOps, você já tentou essa letra!')
            Hangman.checkGuess(self,input('\nChute outra letra: '))
        elif letter.upper() in self.wrong_ans: #checa se letra já não foi usada
            print('\nOps, você já tentou essa letra!')
            Hangman.checkGuess(self, input('\nChute outra letra: '))
        elif letter.lower() in self.word: #se acerta a letra a posição dela na palavra é revelada
            self.right_ans.append(letter.upper())
            for i in range(len(self.word)):
                if letter.lower() == self.word[i]:
                    self.hidden_word[i] = self.word[i].upper()
        else: #se erra a letra enforca mais uma parte
            self.hang += 1
            self.wrong_ans.append(letter.upper())

    def gameStatus(self): #exibe na tela o estado do jogo e pede nova letra se ainda há chances
        os.system('cls')
        print(hanging_stages[self.hang])
        print('\nPalavra: %s' %(''.join(self.hidden_word)))
        print('\nLetras corretas: %s' %(' '.join(self.right_ans)))
        print('\nLetras erradas: %s' %(' '.join(self.wrong_ans)))
        guess = input('\nChute uma letra: ')
        Hangman.checkGuess(self, guess)
        if ''.join(self.hidden_word) == self.word.upper(): #quando jogador acerta todas as letras
            os.system('cls')
            print(hanging_stages[7])
            print('\nParabéns você venceu!')
            print('\nA palavra é %s' %(self.word.upper()))
        elif self.hang == 6: #quando completa a forca e jogador perde
            os.system('cls')
            print(hanging_stages[self.hang])
            print('\nQue pena, você perdeu!')
            print('\nA palavra era %s' %(self.word.upper()))
        else: #se ainda há chances, chama novamente a função
            Hangman.gameStatus(self)

def getWord(): #escolhe palavra aleatoriamente no arquivo txt

    word_bank = open('palavras.txt','r').readlines() #cria uma lista de palavras do arquivo
    choice = random.choice(word_bank).strip('\n') #escolhe uma palavra aleatoriamente
    if len(choice) > 3: #somente aceita palavras com mais de 3 letras
        return choice
    else:
        getWord()

def playAgain(): #função para verificar se o jogador deseja jogar novamente

    new_game = input('\nDeseja jogar novamente? Pressione S para SIM ou N para NÃO\n')
    if new_game.lower() == 's':
        main()
    elif new_game.lower() == 'n':
        print ('\nObrigado por jogar!')
    else: #caso letra não seja 's' ou 'n' pede novamente
        os.system('cls')
        print('\nNão entendi o que você quer. Me diga novamente.')
        playAgain()

def main(): #função para executar o código

    game = Hangman(getWord()) #cria objeto

    game.gameStatus() #roda o jogo

    playAgain() #pergunta se quer jogar novamente

if __name__ == '__main__': #executa o programa
    main()