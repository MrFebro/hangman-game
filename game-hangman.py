
from random import choice
print('')
print('=-' * 30)
print('{:-^60}'.format('HANGMAN BY LUIS FEBRO'))
print('=-' * 30)

def body_hang(c):
  body1 = body2 = body3 = body4 = body5 = body6 = ' '
  if c == 0:
    print('')
  elif c == 1:
    body1 = '(00)'
  elif c == 2:
    body1 = '(00)'
    body2 = '  ||'
  elif c == 3:
    body1 = '(00)'
    body2 = '||'
    body3 = 'o--'
  elif c == 4:
    body1 = '(00)'
    body2 = '||'
    body3 = 'o--'
    body4 = '--o'
  elif c == 5:
    body1 = '(00)'
    body2 = '||'
    body3 = 'o--'
    body4 = '--o'
    body5 = 'o/'
  elif c == 6:
    body1 = '(00)'
    body2 = '||'
    body3 = 'o--'
    body4 = '--o'
    body5 = 'o/'
    body6 = ' \\o'
  print('\n___________')
  print('|         |')       
  print(f'|       {body1}')
  print(f'|     {body3}{body2}{body4}')
  print(f'|       {body5}{body6}  ')
  print('|')
  print('|')
  print('')

################################################################
# DATA BASE - QUESTIONS AND HIDDEN ANSWERS (DO NOT CHEAT HERE (;  )
################################################################
# 5 questions (1º Tip, 2º Answer)
database = ['A brazilian City', 'Rio de Janeiro', 
'Uma cor', 'Yellow',
'A movie', 'Batman', 
'A book', 'Harry Potter', 
'An occupation', 'Programmer']
#choosing data
tips = choice(list(database[n] for n in range(0, len(database), 2))) #here we create only the tips data
answers = database[database.index(tips) + 1].upper()

 
hidden_ans = list(answers)
discovered_letters = []

print(f'\nDICA: {tips}')

for l in range(0, len(hidden_ans)):
  discovered_letters.append(' -- ')
cont = contover = amount = 0
print(f'The word has {len(hidden_ans)} letras. Let's get started!')
body_hang(contover)
print(' -- ' * len(hidden_ans), end = '')
while True:
  user_letter = str(input('\nType a letter: ')).strip().upper()
  if user_letter == '':
    print("It seems like you didn't inserted a letter, pal")
    continue
  if user_letter[0] in '123456789':
    print('Common!!! Numbers are not allowed...just letters')
    continue
  if len(user_letter) > 1:
    print(f'Do you mean {user_letter[0]}, is it not? \nLet's consider the first letter! (=')
    user_letter = user_letter[0]
  #user got one letter
  if user_letter in discovered_letters:
    print('YOu already put this letter. Try again!')
    continue
  if user_letter in hidden_ans:
    body_hang(contover)
    for l in range(0, len(hidden_ans)):
      #inserting the letter into empty list  and replacing ' -- '
      if hidden_ans[l] == user_letter:
        discovered_letters[l] = user_letter
        cont += 1 
      #printing the traces
      print(discovered_letters[l], end = ' ')
  # user not got any letter
  if cont == 0:
    contover += 1
    body_hang(contover)
    print(' -- ' * len(hidden_ans), end = '')  
    # gameover condition
    if contover == 6:
      body_hang(contover)
      print('\nGAME OVER!')
      break
    print('\nNope! ain't got this letter...Try again!')
  # renewed for a new counting
  # cont = 0
  # results 
  print('\nYou guessed {} letters so far! '.format(cont))
  print(f'LEFT: {6 - contover} TRIES...')
    

  #Option to reveal word already with 4 traces left:
  if discovered_letters.count(' -- ') <= 4:
    final_word = ''.join(hidden_ans)
    final_word_user = ' ' 
    while final_word_user not in 'YN':
      final_word_user = str(input('Do you already know the hidden word [Y/N]?  ')).strip().upper()
    if final_word_user == 'Y':
      final_word_user = str(input('You can write over here: ')).strip().upper()
    if final_word == final_word_user:
      print('CONGRATS! YOU GOT IT!')
      break
      print('It seems not the right one...try again...')

  if ' -- ' not in discovered_letters:
    print('CONGRATS! YOU GOT IT!')
    break
print('GAME IS OVER')

# NOTES:
# l means letters. this is requires in both for iteration
