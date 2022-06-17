# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("You")
define t = Character("Tamera")
define ivm = Character("Ivy Mason")
define iv = Character("Ivy")
define rg = Character("Roger Gale")
define r = Character("Roger")
define js = Character("Jasmine Stones")
define j = Character("Jasmine")
define n = Character("Nemo")
define p = Character("Patrick Mason")
define jj = Character("Joshua Jameson")
define sl = Character("Sara Lovelock")
define er = Character("Eileen Riverside")
define als = Character("Alex Svensson")

# Declare character sprites
image ivy side casual frown = im.Scale("Miki/Pose_C/Casual/Miki_PoseC_Casual_Frown.png", 270, 785.4)
image jasmine casual up smile = im.Scale("Hana/Casual/Hana_casual_smile.png", 464.4, 894.6)
image roger casual frown = im.Scale("Sora/Casual/Sora_Casual_Frown.png", 367.2, 924)
image patrick casual smile = im.Scale("Chie/Casual/Chie_Casual_Smile.png", 523, 850)


# The game starts here.

label start:
    
    scene cafeteria_day
    
    "You sit down at a table with a mug of cocoa. For once, it's a quiet day at the café. Perfect for meeting up with Tamera."
    
    "..."
    
    "At least hopefully she is coming. You check your phone. No messages at least yet. Five minutes till you're supposed to meet. She still has time to make it."
    
    "In the meantime, you can enjoy the cocoa."
    
    # TODO Play a notification sound
    
    "You check your phone again. Tamera has sent a message."
    
    t "{i}Sorry, won't be able to make it. Sarah wanted me to hang out. See you some other time{/i}"
    
    "You sigh. Of course this happened again. You really need something else to do... Getting a new friend would be great for starters."
    
    "For the first time since coming to the café, you pay attention to the pamphlet on the table. It advertises a German basics course. Since you need something to do while you finish your cocoa, you start reading."
    
    "The way the pamphlet overtly advertises making friends on the course really rubs salt in your wound, but then again, that could actually be good for you;"
    
    "you'd get something to do other than trying to hang out with Tamera and you might even make new friends to hang out with."
    
    "The -30\% student discount is what finally sells the course. You pick up your phone again and enroll on the course."
    
    "When you pause to check that you're written everything correctly, you notice that autocorrect has messed up both your name and surname. You'd better correct those right away."
    
    python:
        full_name = "Morgan Stevens"
        lesson = 0

        # Initialize the status of notes taken on each lesson. Lesson 0 has no notes, so it can be whatever. True is default for it.
        notes = [True, False, False, False, False, False, False, False, False]
        full_name = renpy.input("Name: ", full_name, length=32)
        full_name = full_name.strip()
        if not full_name:
            full_name = "Morgan Stevens"
        names = full_name.split()
        first_name = names[0]
        if len(names) > 1:
            last_name = names[1]
        else:
            last_name = "Stevens"
            full_name = full_name + " Stevens"
    
    "You send out the form... only for it to bounce back. Apparently, you also need to add your preferred pronouns to avoid misgendering. Well, sure, that sounds fair."
    python:
        pronouns = "unknown"
    
    menu:
        "He/him":
            python:
                pronoun = "he"
                pronoun_refer = "him"
        "She/her":
            python:
                pronoun = "she"
                pronoun_refer = "her"
        "They/them":
            python:
                pronoun = "they"
                pronoun_refer = "them"
    
    "There, all done. Now you just have to wait for confirmation. And finish your cocoa alone."
    
    "This had better be worth it..."
    
    jump classroom
        
return
