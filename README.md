# Hangman game in python using turtle graphics.


```py
WORDBANK:
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
```
---
```py
TURTLE COMMANDS:
t = turtle.Turtle()
s = turtle.getscreen()
t.hideturtle()
#make the gallows
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
#head
t.right(90)
t.circle(20)
#body
t.left(90)
t.penup()
t.forward(40)
t.pendown()
t.forward(50)
#arms
t.back(45)
t.right(45)
t.forward(40)
t.back(40)

t.left(90)
t.forward(40)
t.back(40)
#legs
t.right(45)
t.penup()
t.forward(45)
t.pendown()
t.right(30)
t.forward(50)
t.back(50)

t.left(60)
t.forward(50)
t.back(50)

s.exitonclick()
```
