#import random and turtle
import random
import turtle
#rename turtle to t and screen to s for ease
t = turtle.Turtle()
s = turtle.getscreen()
#list of words that are randomly chosen from
wordList = ["abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure", "bagpipes", "bandwagon","banjo","bayou","beekeeper","bikini","blitz","boggle","bookworm","boxcar",
"buckaroo","buffalo","buffoon","buxom","buzzing","buzzwords","caliph","cobweb","cockiness","croquet","crypt","curacao","daiquiri","dirndl","disavow","dizzying","duplex","dwarves","embezzle",
"equip","espionage","euouae","exodus","faking","fishhook","fixable","flapjack","flopping","fluffiness","flyby","foxglove","frazzled","frizzled","fuchsia","funny","gabby","galaxy","galvanize",
"gazebo","giaour","gizmo","glowworm","glyph","gnarly","gnostic","gossip","grogginess","haiku","haphazard","hyphen","iatrogenic","icebox","injury","ivory","ivy","jackpot","jaundice","jawbreaker",
"jaywalk","jazziest","jazzy","jelly","jigsaw","jinx","jiujitsu","jockey","jogging","joking","jovial","joyful","juicy","jukebox","jumbo","kayak","kazoo","keyhole","khaki","kilobyte","kiosk",
"kitsch","kiwifruit","klutz","knapsack","larynx","lengths","lucky","luxury","lymph","marquis","matrix","megahertz","microwave","mnemonic","mystify","naphtha","nightclub","nowadays","numbskull",
"nymph","onyx","ovary","oxidize","oxygen","pajama","peekaboo","phlegm","pixel","pizazz","pneumonia","polka","pshaw","psyche","puppy","puzzling","quartz","queue","quips","quixotic","quiz",
"quizzes","quorum","razzmatazz","rhubarb","rhythm","rickshaw","schnapps","scratch","shiv","snazzy","sphinx","spritz","squawk","staff","strength","strengths","stretch","stronghold","stymied",
"subway","swivel","syndrome","thriftless","thumbscrew","topaz","transcript","transgress","transplant","triphthong","twelfth","twelfths","unknown","unworthy","unzip","uptown","vaporize","vixen",
"vodka","voodoo","vortex","voyeurism","walkway","waltz","wave","wavy","waxy","wellspring","wheezy","whiskey","whizzing","whomever","wimpy","witchcraft","wizard","woozy","wristwatch","wyvern",
"xylophone","yachtsman","yippee","yoked","youthful","yummy","zephyr","zigzag", "zigzagging", "zilch", "zipper", "zodiac", "zombie"]
#choose a random word from the list
randomWord = random.choice(wordList)
#make all words lower when chosen (all mine are lower already but this will help in the case yours aren't)
randomWord = randomWord.lower()
#create a list for all the letters in  your random word
wordLetters = []
for character in randomWord:
  wordLetters.append(character)
#create a list of used letters
usedLetters = []
#variable to display the letters as an underscore x amount of letters in the word
display = ["_"] * len(wordLetters)
#create difficulties, these change the amount of lives you get and therefore how much of the hangman is already drawn
difficulty = input ("Select the difficulty: 1 (easy), 2 (medium) or 3 (hard): ")
#must accept integers for input
difficulty = int(difficulty)
if difficulty == 1:
  #if easiest difficulty, least amount is already drawn and lives = 10
  lives = 10
  t.hideturtle()
  t.setheading(180)
  t.forward(100)
  t.right(90)
if difficulty == 2:
  lives = 8
  t.hideturtle()
  t.setheading(180)
  t.forward(100)
  t.right(90)
  t.forward(200)
  t.right(90)
  t.forward(100)
if difficulty == 3:
  #if hardest difficulty, most is already drawn and lives = 6
  lives = 6
  t.hideturtle()
  t.setheading(180)
  t.forward(100)
  t.right(90)
  t.forward(200)
  t.right(90)
  t.forward(100)
  t.back(75)
  t.right(135)
  t.forward(35.4)
  t.penup()
  t.back(35.4)
  t.left(135)
  t.forward(75)
  t.pendown()
  t.right(90)
  t.forward(25)

#update display fuction, this shows us when we have letters correct
def updateDisplay(randomWord, display, guess):
  #create indexer which starts at beggining of array
  index = 0
  #while indexer hasn't reached the end of the word...
  while index < len(randomWord):
    #if the letter of the random word at the index matches the inputted letter...
    if randomWord[index] == guess:
      #make the _ at the index now display the correct guessed letter
      display[index] = guess
    #move the indexer along
    index = index + 1
  #return new display
  return display

#start with word being incorrect
wordCorrect = False
#while you haven't run out of lives
while lives > 0: 
  #print the display, lives and used letters
  print (display)
  print ("Lives Left: ", lives)
  print ("Used letters: ", usedLetters)
  #if the display doesn't match the array of letters in the word...
  if display != wordLetters:
    #ask for letter to be guessed, make it lower case and add guessed letter to used letters
    guess = input("Guess a letter: ")
    guess = guess.lower()
    usedLetters.extend(guess)
  #if the guess equals the word or the display has been populated with correct letters...
  if guess == randomWord or display == wordLetters:
    #the word is correct and we finish the program
    wordCorrect = True
    break
  #elsse if the guess is in the array of the word's letters...
  elif guess in wordLetters:
    #update the display using the function created earlier
    display = updateDisplay(randomWord, display, guess)
    #else print that a life is lost, remove a life and update the hangman drawwing using turtle
  else:
    print ("Guess Incorrect. You lose a life")
    lives = lives - 1
    #each life draws an extra part of the drawing, each life corresponds to a line
    if lives == 9:
      #start drawing gallows
      t.forward(200)
      t.right(90)
    if lives == 8:
      t.forward(100)
    if lives == 7:
      t.back(75)
      t.right(135)
      t.forward(35.4)
      t.penup()
      t.back(35.4)
      t.left(135)
      t.forward(75)
      t.pendown()
    if lives == 6:
      t.right(90)
      t.forward(25)
    if lives == 5:
      #draw head
      t.right(90)
      t.circle(20)
    if lives == 4:
      #draw body
      t.left(90)
      t.penup()
      t.forward(40)
      t.pendown()
      t.forward(50)
    if lives == 3:
      #draw arms
      t.back(45)
      t.right(45)
      t.forward(40)
      t.back(40)
    if lives == 2:
      t.left(90)
      t.forward(40)
      t.back(40)
    if lives == 1:
      #draw legs
      t.right(45)
      t.penup()
      t.forward(45)
      t.pendown()
      t.right(30)
      t.forward(50)
      t.back(50)
    if lives == 0:
      t.left(60)
      t.forward(50)
      t.back(50)   

#if the word is correct after the lives have run out then print congratulations
if wordCorrect == True:
  print ("You win, congratulations! The word was", (randomWord))
#if the word is wrong after the lives have run out then print commiserations
if wordCorrect == False:
  print ("You lost, commiserations! The word was", (randomWord))
#make the turtle screen only close on click instead of at the end of the lives
s.exitonclick()