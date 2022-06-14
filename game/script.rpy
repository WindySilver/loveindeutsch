# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen frown
    
    e "So, if the main verb is in the basic form after an auxiliary, verb, 'I can speak German' is... 'Ich kann...' Uh, what was 'speak' again?"

    menu:
        "Sprechen":
            jump correct
        "Sprachen":
            jump wrong
        "I don't know":
            jump idk
        "Let me check my notes":
            jump notes

    return
