from random import choice
print('')
print('=-' * 30)
print('{:-^60}'.format('JOGO DA FORCA'))
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
database = ['Um estado Brasileiro', 'Amazonas', 
'Uma cor', 'Amarelo',
'Um filme', 'Batman', 
'Um livro', 'Segredo', 
'Uma Profissão', 'Programador']
#choosing data
tips = choice(list(database[n] for n in range(0, len(database), 2))) #here we create only the tips data
answers = database[database.index(tips) + 1].upper()

 
hidden_ans = list(answers)
discovered_letters = []

print(f'\nDICA: {tips}')

for l in range(0, len(hidden_ans)):
  discovered_letters.append(' -- ')
cont = contover = amount = 0
print(f'A palavra tem {len(hidden_ans)} letras. Vamos começar!')
body_hang(contover)
print(' -- ' * len(hidden_ans), end = '')
while True:
  user_letter = str(input('\nDigite UMA LETRA: ')).strip().upper()
  if user_letter == '':
    print('Parece que você não digitou uma letra, hein meu.')
    continue
  if user_letter[0] in '123456789':
    print('Vish...Número não pode não...')
    continue
  if len(user_letter) > 1:
    print(f'Você quis dizer {user_letter[0]}, né? \nVou considerar a primeira letra! (=')
    user_letter = user_letter[0]
  #user got one letter
  if user_letter in discovered_letters:
    print('Você já colocou essa letra. Tente Novamente!')
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
    print('\nNão tem essa letra! Tente de Novo!')
  # renewed for a new counting
  # cont = 0
  # results 
  print('\nVocê acertou {} letras até agora! '.format(cont))
  print(f'RESTAM: {6 - contover} Tentativas...')
    

  #Option to reveal word already with 4 traces left:
  if discovered_letters.count(' -- ') <= 4:
    final_word = ''.join(hidden_ans)
    final_word_user = ' ' 
    while final_word_user not in 'SN':
      final_word_user = str(input('Já sabe qual é a Palavra escondida [S/N]?  ')).strip().upper()
    if final_word_user == 'S':
      final_word_user = str(input('Pode escrever aqui: ')).strip().upper()
    if final_word == final_word_user:
      print('PARABÉNS! VOCÊ ACERTOU!')
      break
      print('Parece que não...tente de novo...')

  if ' -- ' not in discovered_letters:
    print('PARABÉNS! VOCÊ ACERTOU!')
    break
print('FIM DO JOGO')

# NOTES:
# l means letters. this is requires in both for iteration