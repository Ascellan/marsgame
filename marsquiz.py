#introducing the game
print("""Welcome, this is a quiz-game that covers facts about the Mars
exploration program of NASA.""")

print("""You made the right choice to be here! You'll learn
so many interesting things about The Red Planet.
""")
#introducing the rules of the game
print("For each category/area, you'll have 5 questions.")
print("""You'll have 1 point for the right answer and 0 points
for the wrong answer.
""")

#TIER 1
#player chooses one of the three options from top category
print("Choose one of the three options, #1, #2 or #3.")
print("""If you change your mind,
you can always come back and choose another topic.""")
print("1. The Planet")
print("2. Science Goals")
print("3. Missions")

#pelaaja valitsee joko 1, 2 tai 3
answer = input("> ")

#jos vastaus on 1
if answer == "1":
    print("""Excellent choice! it's time to learn something about our favourite
    planet Mars.""")
    print("Select one of the options :")
    print("1. Mars facts")
    print("2. Atmosphere")

    #pelaaja valitsee alakategoriasta kahdesta vaihtoehdosta
    answer = input("> ")

    if answer == "1":
        print("""Alright, let's begin the Mars quiz about the fascinating area of
    facts!""")
        print("Question 1:")
        print("What is Mars's average distance from the sun?")
        print("Choose one of the following options:")
        print("1. 55 million miles")
        print("2. 147 million miles")
        print("3. 93 million miles")

#assigning right answer with a value 3
        right_answer = "3"
        #pisteidenlaskuohjelma
        #tää toimii ekalla kierroksella, mut kutsuttaessa
        #toisen kysymyksen jälkeen ei toimi enää,
        #pisteet ei kerry
        #tarvitaan taulukko?
        def points():
            answer = input("> ")
            points = 0
            if answer == right_answer:
                print("That's right!")
                points += 1
                print(f"You've got {points} points now! Excellent!")

            else:
                print("Wrong!")
        points()


        print("Question 2:")
        print("What is the length of the year in Mars (Earth days)?")
        print("Choose one of the following options:")
        print("1. 545 days")
        print("2. 687 days")
        print("3. 421 days")

        right_answer = "2"
        #kutsuu funktiota, funktio ei toimi oikein, tai ei näytä
        #tulostaessa että pisteet lisääntyy tällä kierroksella
        #piste tulee ekaan kysymykseen vastattaessa mutta ei tokaan
        points()





    #player chooses the subcategory atmosphere from the main
    #category "The planet."
    else:
        print("""Alright, let's begin the Mars quiz about the fascinating area of
        Mars atmosphere!""")



elif answer == "2":
    print("Excellent choice! It's time to learn something about Nasa's science goals.")
else:
    print("Excellent choice! It's time to learn something about Nasa's missions to Mars.")
    #def answer(topic1):
        #print("""Alright! it's time to learn some facts about our
        #favourite planet Mars.""")
        #print("This quiz contains overall 10 questions about Mars.")
        #print("""You'll answer either "right" to the question or "wrong".""")
        #print("Your answer will be rated either with one point or zero points.")
        #print("""You'll get one point from right answer and zero points from
        #the wrong answer.""")






#question1 = input("Do you want to learn something about ")
