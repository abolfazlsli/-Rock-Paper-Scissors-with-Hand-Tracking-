from photo import * # get photo from https://github.com/abolfazlsli/photo
import pyttsx3
import random,time
import threading
x = photograph()
y = handDetector()
choicelist = ['r','p','s']
e = pyttsx3.init()
e.setProperty('rate',130)
text = "hello human ."
e.say(text)
e.runAndWait()
text2 = "lets play a game ."
e.say(text2)
e.runAndWait()
def check_win(choice , c):
    if (choice == "r" and c == "s") or (choice == "p" and c == "r") or (choice == "s" and c == "p"):
        text = "you win"
        e.say(text)
        e.runAndWait()
        print("you win .")
    elif (choice == "s" and c == "r") or (choice == "p" and c == "s") or (choice == "r" and c == "p"):
        text = "I win"
        e.say(text)
        e.runAndWait()
        print("i win")
    else:
        text = "no win"
        e.say(text)
        e.runAndWait()
        print("no win")
    print(choice , c)
    text = "lets playe again"
    e.say(text)
    e.runAndWait()
say = False
def mainapp():
    while True:
        if not say:
            text = "all right i choice your turn."
            e.say(text)
            e.runAndWait()
            c = random.choice(choicelist)
            say = True
        img = x.camera()
        y.findHands(img)
        y.findPosition(img)
        try:
            t = y.fingersUp()
            # print(t)
            point = 0
            for i in t:
                if i == 1:
                    point += 1
            if point <=  1:
                choice = "r"
            elif point == 2:
                choice = "s"
            elif point == 5:
                choice = "p"
            check_win(choice,c)
            say = False
        except:
            pass

    # e = x.show(img)
    # if e == ord("q"):
    #     break

    # print(data)

