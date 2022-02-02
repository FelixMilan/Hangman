import random
import turtle

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

#variables needed for game
selectedWord = random.choice(wordList)
selectedWord = selectedWord.lower()
selectedLetters = []
usedLetters = []
guessedLetters =[]
playerWin = False


#make the guessedLetters have the right amount of missing spaces and the selectedLetters have the right Letters
for Letters in selectedWord:
    selectedLetters.append(Letters)
    guessedLetters += "_"

#create difficulties, these change the amount of lives you get and therefore how much of the hangman is already drawn
while True:
    try:
        difficulty = input ("Select the difficulty: 1 (easy), 2 (medium) or 3 (hard): ")
        difficulty = int(difficulty)
        if(difficulty < 1 or difficulty > 3):
            print ("Please select either the difficulty: 1 (easy), 2 (medium) or 3 (hard):")
        else:
            print ("Difficulty " + str(difficulty) + " selected.")
            break
    except ValueError:
        print ("Not a valid difficulty, please try again")
        
if difficulty == 1:
  #if easiest difficulty, least amount is already drawn and lives = 10
  lives = 10
  t.hideturtle()
  t.setheading(180)
  t.forward(100)
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

#updateGuessedLetters fuction, this shows us when we have letters correct
def updateGuessedLetters(selectedWord, guessedLetters, guess):
  for index in range(0,len(selectedWord)):
    if selectedWord[index] is guess:
        guessedLetters[index] = guess
  return guessedLetters

def alreadyGuessed(guess):
    for letters in usedLetters:
        if guess is letters:
            return True
    return False

def getValidGuess(guess):
    while alreadyGuessed(guess) and len(guess) is 0:
        if len(guess) is 0:
            guess = input("Please enter a letter")
        else:
            guess = input("Letter has already been guessed, enter a new letter: ")
    return guess

#main game logic
while lives > 0 or playerWin: 
    #print stats
    print (guessedLetters)
    print ("Lives Left: ", lives)
    print ("Used letters: ", usedLetters)

    #input and verify guess
    guess = input("Guess a letter: ")   
    guess = getValidGuess(guess)

    #add verified guess to used letters
    usedLetters.extend(guess[0])
    usedLetters.sort()
    
    if guessedLetters is selectedLetters:
        playerWin = True
    #if guess correct update guessed letters to contain it
    elif guess in selectedLetters:
        guessedLetters = updateGuessedLetters(selectedWord, guessedLetters, guess)
    #incorrect guess results in loss of 1 life
    else:
        print ("Guess Incorrect. You lose a life")
        lives -= 1
        if lives == 9:
        #start drawing gallows
            t.right(90)
            t.forward(200)
        if lives == 8:
            t.right(90)
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

#win/lose screens
if playerWin is True:
    print ("You win, congratulations! The word was", (selectedWord))

if playerWin is False:
    print ("You lost, commiserations! The word was", (selectedWord))
