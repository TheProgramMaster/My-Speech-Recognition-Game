import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()
def getSpeech():
    with mic as sr:
        print("Please speak")
        r.adjust_for_ambient_noise(sr)
        audio = r.listen(sr)
        speech = r.recognize_google(audio)
        return speech

print("You are in a forest with three paths. In front of you is a city, wherein there appears to be a kingdom in the distance.")
print("On your left, there appears to be a mystical river.")
print("On your right, there appear to be a magical hut.")
print("Which path will you take? (Please state either 'forward', 'left', or 'right' in one word.)")
choice1 = getSpeech()
while(str(choice1) != "left" and str(choice1) != "forward" and str(choice1) != "right"):
    print("Sorry, but choice given is invalid, please try again.")
    print("Say either 'left', 'forward', or 'right'")
    choice1 = getSpeech()

if(str(choice1) == "left"):
    print("You turn to your left to walk down the path to the mystical river. As you approach the river, you find a magical sword in the river, and a hut next to the river.")
    print("Do you pick up the sword, enter the hut, or continue on your way? (Please say either 'sword', 'hut', or 'continue').")
    choice2 = getSpeech()
    while(str(choice2) != "hut" and str(choice2) != "sword" and str(choice2) != "continue"):
        print("Sorry, but choice given is invalid, please try again.")
        print("Say either 'hut', 'sword', or 'continue'.")
        choice2 = getSpeech()
    if(str(choice2) == "hut"):
        print("Yoou enter the hut and find a wizard concocting a potion in his magical cauldron.");
        print("He tells you that he is making a potion to make food appear, but he needs help determining the final ingredient.")
        print("He points to a shelf in his room and there are three items.")
        print("The items given are an elephant nose, a healthy carrot, and a gemstone.")
        print("Which item do you give him? (Please say either 'nose', 'carrot', or 'gem').")
        choice3 = getSpeech()
        while(str(choice3) != "nose" and str(choice3) != "carror" and str(choice3) != "gem"):
            print("Sorry, but choice given is invalid, please try again.")
            print("Say either 'nose', 'carrot', or 'gem'.")
            choice3 = getSpeech()
        if(str(choice3) == 'nose'):
            print("You give the magician the elephant nose to put in the cauldron. He mixes the potion, produces a vial of the concoction, and offers for you to drink it. You do so.")
            print("Upon consuming the potion, you look in a nearby mirror and find your appearance resembles that of an elephant. Perhaps that was the wrong potion...")
            print("THE END")
        else if(str(choice3) == 'carrot'):
            print("You give the magician the healthy carrot to put in the cauldron. He mixes the potion, produces a vial of the concoction, and offers for you to drink it. You do so.")
            print("Upon consuming the potion, you walk outside of the hut and reach your hand out to the ground, pointing to s nearby spot on the ground. A bush of vegetables and fruit immediately begins to flourish.")
            print("Well done! You made the correct concoction and have solved world hunger with magic!")
            print("THE END")
        else if(str(choice3) == 'gem'):
            print("You give the magician the gemstone to put in the cauldron. He mixes the potion, produces a vial of the concotion, and offers for you to drink it. You do so.")
            print("Upon consuming the potion, you walk outside of the hut and immediately reach out your hand to point at the ground. You point at the ground, and a rock full of gemstones immediately begins to rise out of the ground.")
            print("You appear to have made the wrong concoction. While you may have failed in your efforts to solve world hunger, you can now create all the valuable gemstones at will!")
            print("THE END")
    else if(str(choice2) == "sword"):
        print("You walk to the brink of the river and sit down to pick up the sword. As you pick up the sword, you feel a magical force.")
        print("A magical being immediately appears before you. It tells you that the sword is cursed and was a possession of its family. He thereby asks you to return it.")
        print("Will you return the sword, keep it, or destroy it? (Please say either 'return', 'keep', or 'destroy').")
        choice3 = getSpeech()
        while(str(choice3) != 'sword' and str(choice3) != 'keep' and str(choice3) != 'destroy'):
            print("Sorry, but choice given is invalid, please try again.")
            print("Say either 'return', 'keep', or 'destroy'.")
            choice3 = getSpeech()
        if(str(choice3) == "return"):
            print("You relinquish the sword, returning it to the river. The spirit thanks you for your kindness.")
            print("You walk back the way you came, feeling all the happier for having done the right thing.")
            print("THE END")
        else if(str(choice3) == "keep"):
            print("You tell the spirit you intend to keep the sword. He becomes upset and places a curse on you.")
            print("The sword becomes sticker. The spirit then tells you that the sword will never leave your hand for as long as you shall live.")
            print("Perhaps it would have been better to simply have let go of the sword.")
            print("THE END")
        else if(str(choice3) == "destroy"):
            print("You take the sword and shatter it by hitting it against the stones nearby the river. The spirit becomes furious.")
            print("The spirit then takes the shards of the sword and re-molds them into a pair of shoes. The shoes them appear on your feet.")
            print("The spirit now controls where you will go for the rest of your life. Perhaps it would have been better to have simply let the sword go.")
            print("THE END")
    else if(str(choice2) == "continue"):
        print("You continue on your way down the path of the mystical river. As you do so, you find a chest. Do you open it, walk away, or throw it?")
        print("Please say either 'open', 'walk', or 'throw'.")
        choice3 = getSpeech()
        while(str(choice3) != 'open' and str(choice3) != 'walk' and str(choice3) != 'throw'):
            print("Sorry, but choice given is invalid, please try again.")
            print("Say either 'open', 'walk', or 'throw'.")
            choice3 = getSpeech()
        if(str(choice3) == "open"):
            print("You open the chest and find a mountain of gold inside. You take all of it and stuff it into your backpack.")
            print("Walking home, you cannot wait to eat all of the food you can consume with your newfound wealth!")
            print("THE END")
        else if(str(choice3) == "walk"):
            print("Thinking the opportunity risky, you decided to turn around and walk back home.")
            print("As you do so, you cannot help but wonder what may have been hidden in that chest.")
            print("THE END")
        else if(str(choice3) == "throw"):
            print("Thinking that something dangerous may be in the chest, you decide to pick it up and throw it in the river.")
            print("In doing so, you notice that the chest comes apart while hitting the river. A mountain of gold rises to the surface.")
            print("If only you had chosen to open that chest...")
            print("THE END")
else if(str(choice1) == "forward"):
    print("You choose to walk forward on the path to city wherein the kingdom is located.")
    print("As you walk into the city, you notice there is an inn, the castle itself, and a garden nearby.")
    print("Where do you go? (Please say either 'inn', 'castle', or 'garden')")
    choice2 = getSpeech()
    while(str(choice2) != 'inn' and str(choice2) != 'castle' and str(choice2) != 'garden'):
        print("Sorry, but choice given is invalid, please try again.")
        print("Say either 'inn', 'castle', or 'garden'")
        choice2 = getSpeech()
    if(str(choice2) == 'inn'):
        print("You decide to walk into the inn. You pay the inn keeper to stay the night.")
        print("Upon waking up the following morning, you decide to sit down to eat the day's breakfast.")
        print("As you do so, a young man walks in. He claims that goblins have broken into the city and are now robbing a nearby citizen in their home.")
        print("Do you remain eating, help the family that is being robbed, or flee the city for your own safety? (Please say either 'eat', 'help', or 'flee')")
        choice3 = getSpeech()
        while(str(choice3) != 'eat' and str(choice3) != 'help' and str(choice3) != 'flee'):
            print("Sorry, but choice given is invalid. Please try again.")
            print("Please say either 'eat', 'help', or 'flee'.")
            choice3 = getSpeech()
        if(str(choice3) == "eat"):
            print("You decide to remain eating while the family is being robbed.")
            print("Walking out upon completion of your meal, you feel guilty for refusing to do the right thing when given the chance.")
            print("THE END")
        else if(str(choice3) == "help"):
            print("You decide to help the family in their time of need. Dashing out of the inn, you grab a sword found at the door and rush to the scene of the crime.")
            print("When you arrive at the house, you defeat all of the goblins and save the family. The kingdom rejoices in your act of courage!")
            print("THE END")
        else if(str(choice3) == "flee"):
            print("Considering your own safety in light of the presence of goblins, you choose to flee.")
            print("As you leave the kingdom, you feel guily at the though of having left the family in their time of need...")
            print("THE END")
    else if(str(choice2) == 'castle'):
            print("You decide to visit the castle today. You walk up to the castle's front door and knock on the door.")
            print("A guard appears to let you in. You see the king and queen, who tell you there is a problem concerning an invading army in the distance.")
            print("Do you draw up plans with which to defend the kingdom, walk away, or find help? (Please say either 'draw', 'walk', or 'help').")
            choice3 = getSpeech()
            while(str(choice3) != "draw" and str(choice3) != "walk" and str(choice3) != "help"):
                print("Sorry, but choice given is invalid. Please try again.")
                print("Please say either 'draw', 'walk', or 'help'.")
                choice3 = getSpeech()
            if(str(choice3) == "draw"):
                print("You immediately begin to draw up plans to defend the kingdom by instructing how to guard the city walls most effectively.")
                print("The king takes these plans and accepts them. He immediately promotes you to captain of the kingdom army. Good job!")
                print("THE END")
            else if(str(choice3) == "walk"):
                print("Thinking the matter beyond your capabilities, you decide to simply walk away.")
                print("As you do so, you cannot help but think you may have been able to help the kingdom in some way...")
                print("THE END")
            else if(str(choice3) == "help"):
                print("While you do not think you will be able to to help the kingdom directly, you set out to find someone who can.")
                print("You locate the court intellectual who drafts plans to defend the kingdom from the invading army.")
                print("The king promotes the court intellectual to the position of captain of the kingdom army.")
                print("Thinking back on it, though, you cannot help but think you could be standing in place of the court intellectual if you had acted differently...")
                print("THE END")
    else if(str(choice2) == 'garden'):
        print("You decide to travel to a nearby garden that is being cared for by one of the kingdom's citizens.")
        print("You notice that the garden has a collection of vegetables, fruits, and all other plant foods.")
        print("Then citizen who cares for the garden tells you they need you to help them in getting fertilizer for the seasons' harvest.")
        print("Do you help them, walk away, or ask for food? (Please say either 'help', 'walk', or 'eat').")
        choice3 = getSpeech()
        while(str(choice3) != 'help' and str(choice3) != 'walk' and str(choice3) != 'eat'):
            print("Sorry, but choice given is invalid. Please try again.")
            print("Please say either 'help', 'walk', or 'eat'")
            choice3 = getSpeech()
        if(str(choice3) == "help"):
            print("You choose to help the citizen. You walk to a nearby store and purchase as much fertilizer as you can.")
            print("When you return to the citizen and give them the fertilizer, they pay you a mountain of gold for your work. Good job!")
            print("THE END")
        else if(str(choice3) == "walk"):
            print("Thinking the matter to be too much work, you decide to decline the citizens'request for help and continue walking on your way.")
            print("Walking away, you cannot help but think you could have helped the citizen in need...")
            print("THE END")
        else if(str(choice3) == "eat"):
            print("You decide to ask the citizen if you can take some of their food instead to eat. They tell you they will not unless you help them.")
            print("As you do not want to help, you decide to continue walking on your way. If only you had helped that citizen in need...")
            print("THE END")
else if(str(choice1) == "right"):
    print("You decide to walk to your right on the way to the magical hut.")
    print("As you do so, you find that there is the hut, a nearby library, and a cave.")
    print("Where do you go? (Please say either 'hut', 'library', or 'cave'")
    choice2 = getSpeech()
    while(str(choice2) != 'hut' and str(choice3) != 'library' and str(choice3) != 'cave'):
        print("Sorry, but the choice given is invalid. Please try again.")
        print("Please say either 'hut', 'library', or 'cave'.")
        choice2 = getSpeech()
    if(str(choice2) == "hut"):
        print("You approach the hut and knock on the front door of the building. A magical wizard appears. He tells you he is working on a spell and needs help.")
        print("He explains that the spell he is working on will allow him to cure a disease, but he needs a particular item.")
        print("Do you help him, walk away, or ask if he can work on a spell for you? (Please say either 'help', 'walk', or 'request').")
        choice3 = getSpeech()
        while(str(choice3) != 'help' and str(choice3) != 'walk' and str(choice3) != 'request'):
            print("Sorry, but choice given is invalid. Please try again.")
            print("Please say 'help', 'walk', or 'request'")
            choice3 = getSpeech()
        if(str(choice3) == "help"):
            print("You decide to help the wizard in his efforts to cure a disease. He asks you to retrieve a gemstone near the building.")
            print("You do so. The wizard them takes the gemstone and mixes it into a vial containing a potion. He drinks it and feels much better.")
            print("He has cured his illness!")
            print("THE END")
        else if(str(choice3) == "walk"):
            print("You decide not to help the wizard.")
            print("As you walk away, you cannot help but think you could have helped the wizard with an amazing potion...")
            print("THE END")
        else if(str(choice3) == "request"):
            print("You decide instead to ask the wizard if they can work on a spell for you. They agree to do so.")
            print("You request of the wizard to create a potion that will make you taller. When they finish doing so, you drink the potion.")
            print("You immediately notice the world around you get larger. Apparently the wizard mixed up the potions. Perhaps this goes to show it is better to help than to receive...")
            print("THE END")
    else if(str(choice2) == "library"):
        print("You take notice of the nearby library and decide to enter it. You find a werewolf attend the front counter of the establishment.")
        print("They ask you to help them in reorganizing the bookshelves.")
        print("Do you help them, leave the library, or decide to browse the library? (Please say either 'help', 'leave', or 'browse').")
        choice3 = getSpeech()
        while(str(choice3) != "help" and str(choice3) != "leave" and str(choice3) != "browse"):
            print("Sorry but choice given is not valid. Please try again.")
            print("Please say either 'help', 'leave', or 'browse'.")
            choice3 = getSpeech()
        if(str(choice3) == 'help'):
            print("You decide to help the werewolf as they attempt to reorganize the bookshelves of the library.")
            print("After you spend the day doing so, they reward you with a collection of interesting books to take home and read.")
            print("THE END")
        else if(str(choice3) == 'leave'):
            print("You decide to leave the library rather than stay or help the werewolf.")
            print("You fell as though the library would have been an interesting experience had you stayed.")
            print("THE END")
        else if(str(choice3) == 'browse'):
            print("You refuse to help the werewolf and choose instead to browse the library. In doing so, you find a cursed book.")
            print("The book places a curse on you in which you must stay in the library forever. Perhaps it would have been better to help the werewolf.")
            print("THE END")
    else if(str(choice2) == "cave"):
        print("You take notice of the cave and decide to go in. You notice that the cave is dark and you can either go on a path to your left, right, or forward.")
        print("Which path do you go down? (Please say either 'left', 'forward', or 'right'")
        choice3 = getSpeech()
        while(str(choice3) != "left" and str(choice3) != "forward" and str(choice3) != "right"):
            print("Sorry, but choice given is invalid. Please try again.")
            print("Please say either 'left', 'forward', or 'right'.")
            choice3 = getSpeech()
        if(str(choice3) == "left"):
            print("You decide to walk down the path to your right. You find an individual who has been trapped in the cave for a long time.")
            print("Guiding them out of the cave, you feel greatful to have helped this individual in their time of need.")
            print("THE END")
        else if(str(choice3) == "forward"):
            print("You decide to walk down the path in front of you. You find a treasure chest and open it.")
            print("Inside the chest is a mountain of gold. You collect all of it and return home. Good job!")
            print("THE END")
        else if(str(choice3) == "right"):
            print("You decide to walk down the path to your right. You find a trap door beneath you.")
            print("You notice you are now in a trap room. It appears you are stuck here until someone else comes to help you.")
            print("THE END")
