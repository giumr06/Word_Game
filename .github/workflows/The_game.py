import random
import emoji

first_list =[]
with open('first_list.txt') as f:
  lines = f.read().splitlines()
  first_list = lines
  
word = random.choice(first_list)

def pr_red(text): 
  return ("\033[31m\033[01m {}\033[00m" .format(text))
  

def pr_green(text): 
  return ("\033[92m\033[01m {}\033[00m" .format(text))
  

def pr_cyan(text): 
  return ("\033[36m\033[01m {}\033[00m" .format(text))




print (("---------")*6)
print ("Hi!" + emoji.emojize("🖖") +"Welcome to our version of a certain famous word-guessing game.To play is simple: Choose a 5 letters word and see if its the same word we had choosen. You have 6 chances.") 
print("Good luck!" + emoji.emojize("🍀"))
print("                -------------------")
print("                    Color index:")
print(" ")
print(pr_green("Right guess!"))
print(pr_cyan("This letter exists in the word but not in this position."))
print(pr_red("Wrong guess. Try another letter."))
print (("---------")*6)
print(" ")

#--------------------------------------------------

def printing_the_game (word, message):
  space1 = "-----"
  space2 = "|" + " |".join(word)
  print(space1*4)
  print(str(space2) + " | " + message)
  print(space1*4)


def wrong_guess (guess_word, computer_word):
  result_list = []
  for i in range(0, len(guess_word)):
    if guess_word[i] == computer_word [i]:
      a = pr_green(guess_word[i])
      result_list.append(a)
    elif guess_word[i] in computer_word:
      b = pr_cyan(guess_word[i])
      result_list.append(b)
    else: 
      c = pr_red(guess_word[i])
      result_list.append(c)
      
  printing_the_game(result_list, "")



def the_game():
  for x in range (0,6):
     guess = input("Choose a 5 letters word:").lower().replace(" ", "")
     if len(guess) > 5:
       print("Your word needs to have 5 letters. This one is too long.") 
       continue
     if len(guess) < 5:
       print("Your word needs to have 5 letters. This one is too short.")
       continue
     if guess == word:
       list = []
       x = pr_green(guess)
       list.append(x)
       printing_the_game(list, "You won!"+ emoji.emojize("🥳"))
       break
     if guess != word:
        wrong_guess(guess, word)
  
  if guess != word:
     print("Game Over!"+ emoji.emojize("💥"))
     print("The word was: " + str(word))


#---------------------------------------------------



the_game()

print(" ")
replay = input("Do you want to play again?").lower().replace(" ", "")
print(" ")
while replay == "yes" or replay == "yeap" or replay == "y" or replay == "yah":
   word = random.choice(first_list)
   the_game()
   replay = input("Do you want to play again?").lower().replace(" ", "")
  
if replay == "no" or replay == "nah" or replay == "nope" or replay == "nope" or replay == "n":
 print("Ok! See you next time."+ emoji.emojize("👋"))
