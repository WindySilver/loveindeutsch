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

label classroom:
    
    scene classroom_day
    
    if lesson == 0:
        
        show patrick casual smile at left
        
        "Teacher" "Hello and welcome to German Basics. I'm glad to see so many of you here. My name is [p]. If you need to refer to me with pronouns, please use he/him."
        
        p "First, let's have a roll call so I can connect the names to your faces. Joshua Jameson?"
        
        "An old man" "Present."
        
        p "[full_name]?"
        
        y "Here."
        
        p "Sara Lovelock?"
        
        "A black-haired woman" "Here!"
        
        p "[ivm]?"
        
        "Mason? Are they related?"
        
        "A blonde girl rolls her eyes with a sigh."
        
        show ivy side casual frown at right
        ivm "Present."
        
        "You cannot say that they look similar. Perhaps it's just a coincidence that they share the surname?"
        
        hide ivy side casual frown
        
        p "Eileen Riverside?"
        
        "A middle-aged woman" "Present."
        
        p "[js]?"
        
        "The quiet chatter you've been ignoring so far behind you pauses. You glance over your shoulder at two other students."
        
        show jasmine casual up smile at right
        
        js "Here!"
        
        hide jasmine casual up smile
        
        p "Please have your conversation with your friend when the lesson isn't ongoing, Stones. [rg]?"
        
        "The facepalming guy next to Jasmine speaks up."
        
        show roger casual frown at right
        
        rg "Present..."
        
        hide roger casual frown
        
        p "The same instructions to you as well, Gale."
        
        p "And last but not least, Alex Svensson."
        
        "A younger man" "Here."
        
        "Patrick nods."
        
        p "Good. I can't promise I'll remember all the names correctly by the end of the lesson, but I'll try. First, how about we all tell how we ended up here?"
        
        p "I'll go first. I mean, I am here because that's what my work agreement told me to do."
        
        p "Heh. Humor aside, I ended up becoming a German teacher after I spent time as an exchange student in Switzerland."
        
        p "I was already studying to become a language teacher, but at the time I was majoring in Latin. I ended up finding a truer passion for German, however, and now I am here."
        
        p "That's my story. Who wants to go next?"
    
    return
