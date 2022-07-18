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
define e = Character("Everyone")

# Declare character sprites
image ivy side casual frown = im.Scale("Miki/Pose_C/Casual/Miki_PoseC_Casual_Frown.png", 270, 785.4)
image ivy side casual smile = im.Scale("Miki/Pose_C/Casual/Miki_PoseC_Casual_Smile.png", 270, 785.4)
image jasmine casual up smile = im.Scale("Hana/Casual/Hana_casual_smile.png", 464.4, 894.6)
image jasmine casual up frown = im.Scale("Hana/Casual/Hana_casual_neutral.png", 464.4, 894.6)
image roger casual frown = im.Scale("Sora/Casual/Sora_Casual_Frown.png", 367.2, 924)
image roger casual frown blush = im.Scale("Sora/Casual/Sora_Casual_Frown_Blush.png", 367.2, 924)
image roger casual smile = im.Scale("Sora/Casual/Sora_Casual_Smile.png", 367.2, 924)
image roger casual smile blush = im.Scale("Sora/Casual/Sora_Casual_Smile_Blush.png", 367.2, 924)
image roger casual open = im.Scale("Sora/Casual/Sora_Casual_Open.png", 367.2, 924)
image roger casual open blush = im.Scale("Sora/Casual/Sora_Casual_Open_Blush.png", 367.2, 924)
image patrick casual smile = im.Scale("Chie/Casual/Chie_Casual_Smile.png", 523, 850)
image patrick casual frown = im.Scale("Chie/Casual/Chie_Casual_Frown.png", 523, 850)


# The game starts here.

label start:
    init: 
        transform flip: 
            xzoom -1.0
    python:
        # Initialize the status of notes taken on each lesson. Lesson 0 has no notes, so it can be whatever. True is default for it.
        notes = [True, False, False, False, False, False, False, False, False]

        # If character's approval level falls to this number, they will stop wanting to spend time with you. The player cannot recover from hitting this.
        abandon_level = 0
        ivy_abandon = False
        roger_abandon = False
        jasmine_abandon = False

        # Needed for checking if the characters have reached friendship or romance
        ivy_friend = False
        ivy_romance = False
        roger_friend = False 
        roger_romance = False
        jasmine_friend = False
        jasmine_romance = False

        # Needed for tracking whether or not the player has rejected the romance from a character
        ivy_reject = False
        roger_reject = False
        jasmine_reject = False

        # The lowest neutral approval levels for each character, needed for comparisons that need to be made during the game. 
        ivy_approve_neutral_low = 3
        roger_approve_neutral_low = 5
        jasmine_approve_neutral_low = 7

        # The lowest friendship approval levels for each character, needed for comparisons that need to be made during the game. 
        ivy_approve_friend_low = 5 # The one in final version should be 11 but for the short prototype it'll be lower
        roger_approve_friend_low = 7 # The one in final version should be 10 but for the short prototype it'll be lower
        jasmine_approve_friend_low = 8 # The one in final version should be 9 but for the short prototype it'll be lower

        # The lowest romance approval levels for each character, needed for comparisons that need to be made during the game. 
        ivy_approve_romance_low = 8 # The one in final version should be 20 but for the short prototype it'll be lower
        roger_approve_romance_low = 10 # The one in final version should be 18 but for the short prototype it'll be lower
        jasmine_approve_romance_low = 10 # The one in final version should be 16 but for the short prototype it'll be lower

        # The approval trackers for the characters. Set to the lowest neutral as default in the beginning.
        ivy_approve = ivy_approve_neutral_low
        roger_approve = roger_approve_neutral_low
        jasmine_approve = jasmine_approve_neutral_low
        
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

label all_approve:
    python:
        if not roger_abandon:
            roger_approve += 1
        if not jasmine_abandon:
            jasmine_approve += 1
        if not ivy_abandon:
            ivy_approve += 1
    return
        

label all_disapprove:
    python:
        roger_approve -= 1
        jasmine_approve -= 1
        ivy_approve -= 2
    return