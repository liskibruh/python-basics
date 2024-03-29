import sys, random

def main():
    print("Welcome to the Psych 'Sidekick Name Picker'.\n")
    print("A name just like Sean would pick for Gus:\n\n")

    first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie­Weenie'", "Bob 'Stinkbug'", \
        'Bowel Noises', 'Boxelder', 'Butterbean', 'Buttermilk', 'Buttocks', \
        'Chad', 'Chesterfield', 'Chewy', 'Chigger", "Cinnabuns', 'Cleet', 'Cornbread', \
        'Crab Meat', 'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',\
        'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim' )

    last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom', 'Breedslovetrout', \
        'Butterbaugh', 'Clovenhoof', 'Clutterbuck', 'Cocktoasten', 'Endicott', 'Fewhairs', \
        'Gooberdapple', 'Goodensmith', 'Goodpasture', 'Guster', 'Henderson', 'Hooperbag',\
        'Hoosenater', 'Hootkins', 'Jefferson', 'Jenkins', 'Jingley­Schmidt', 'Johnson', \
        'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles', 'Noseworthy',\
        'Olivetti', 'Outerbridge', 'Overpeck')

    while True:
        first_name = random.choice(first)
        last_name = random.choice(last)
        print("\n\n")
        print(f"{first_name, last_name}", file=sys.stderr)
        print("\n\n")
        try_again = input("\n\nTry again? (Press Enter else n to quit.)\n")
        if try_again == "n":
            break
    input("\nPress Enter to exit.")
    
if __name__ == "__main__":
    main()