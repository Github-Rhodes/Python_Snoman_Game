import random

class Word:
  def __init__(self, chosen_word):
    self.chosen_word = chosen_word
    self.guess_list = []

  def word_split(self):
    for i in self.chosen_word:
      new_letter = {
        'letter': i,
        'been_guessed': False
      }
      self.guess_list.append(new_letter)
    return self.guess_list


alpha_check = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']

remaining_guesses = 8
letters_used = []
game_status = []
guessed_so_far = []

random_words = ['Python', 'React', 'Swift', 'Angular', 'Mongoose', 'node', 'heroku', 'vscode', 'general', 'assembly', 'Xcode', 'Flask', 'Express', 'bootsrap', 'GitHub' ]

word = Word(random.choice(random_words))
word_list = word.word_split()


for i in range(len(word_list)):
  letters_used.append(word_list[i]['letter'])
  game_status.append('_')


while remaining_guesses > -1:
  if remaining_guesses == 0:
    print("\nGame over! You lose!\n")
    remaining_guesses -= 1
  elif ''.join(game_status) == ''.join(letters_used):
    print("*")
    print("   *")
    print("      *")
    print("         *")
    print("            *")
    print("              **YOU DID IT!**")
    print("\nThe word was:", ''.join(letters_used))
    print("\nThanks for playing!\n")
    break
  else:
    if len(guessed_so_far) > 0:
      print(f"Letter used so far: {', '.join(guessed_so_far)}\n")
    print(f"You have {remaining_guesses} guesses left. The word is:\n")
    print(' '.join(game_status))
    guess = input('\nGuess a letter (or type GUESS to solve): ')
    if guess == 'GUESS':
      solve = input("\nEnter solution: ")
      if solve.lower() == ''.join(letters_used).lower():
        for i in range(len(game_status)):
          game_status[i] = letters_used[i]
      else:
        remaining_guesses = 0
    elif len(guess) > 1 or guess not in alpha_check:
      print("\nPlease enter a single letter. Try again.\n")
    elif guess.lower() in guessed_so_far or guess.upper() in guessed_so_far:
      print('\nYou already guessed that. Try again.\n')
    elif guess.lower() in letters_used or guess.upper() in letters_used:
      print('\nCorrect!\n')
      for i in range(len(game_status)):
        if letters_used[i] == guess.lower() or letters_used[i] == guess.upper():
          game_status[i] = letters_used[i]
      guessed_so_far.append(guess)
    else:
      print('\nWrong!\n')
      guessed_so_far.append(guess)
      remaining_guesses -= 1
