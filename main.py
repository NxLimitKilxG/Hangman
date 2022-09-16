print('Welcome to Hangman, win the game by guessing all the correct letters. Lose the game by guessing more than 6 incorrect letters.') 


word = 'cake'


print("Guess the Word")

guesses = ''
#The letters go in here

turns = 6


while turns > 0:
  #while the game is still going:
  
  failed = 0

  for char in word:
    
  
    if char in guesses:
      print(char)
      #if the user guessed a correct letter it will print that letter in the correct spot
    else:
      print("_")
      

      failed = failed + 1
      #if the user inputted an incorrect letter it will add 1 to the value of failed
      

  if failed == 0:
    
    print("You Win!")
    
  
    print("The word is: ", word)
    break
  

  guess = input("Guess the correct letter: ")
  

  guesses += guess 
  

  if guess not in word:
  #If the guess isnt in the word then its wrong 
      
    turns = turns - 1
    #removes one turn every time the user guesses a wrong letter
    
    print("Bad Letter")
    #tells the user the letter is bad
  
    print("You have", + turns, 'more guesses')
    #tells the user how many more guesses and turns that they have.
    
    if turns == 0:
       print("You Lose!")
       #tells the user that they lost
    










