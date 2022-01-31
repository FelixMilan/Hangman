import random

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


#make the guessedLetters have the right ammount of missing spaces and the selectedLetters have the right Lettersecters
for Lettersacter in selectedWord:
    selectedLetters.append(Lettersacter)
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
        
if difficulty is 1:
    lives = 10
if difficulty is 2:
    lives = 8
if difficulty is 3:
    lives = 6

#update guessedLetters fuction, this shows us when we have letters correct
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

#win/lose screens
if playerWin is True:
    print ("You win, congratulations! The word was", (selectedWord))

if playerWin is False:
    print ("You lost, commiserations! The word was", (selectedWord))
