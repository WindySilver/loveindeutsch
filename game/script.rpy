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
        
        "Teacher" "Guten Tag! Welcome to German Basics. I'm glad to see so many of you here. My name is [p]. If you need to refer to me with pronouns, please use he/him."
        
        p "First, let's have a roll call so I can connect the names to your faces. [jj]?"
        
        "An old man" "Present."
        
        p "[full_name]?"
        
        y "Here."
        
        p "[sl]?"
        
        "A black-haired woman" "Here!"
        
        p "[ivm]?"
        
        "Mason? Are they related?"
        
        "A blonde girl rolls her eyes with a sigh."
        
        show ivy side casual frown at right
        ivm "Present."
        
        "You cannot say that they look similar. Perhaps it's just a coincidence that they share the surname?"
        
        hide ivy
        
        p "[er]?"
        
        "A middle-aged woman" "Present."
        
        p "[js]?"
        
        "The quiet chatter you've been ignoring so far behind you pauses. You glance over your shoulder at two other students."
        
        show jasmine casual up smile at right
        
        js "Here!"
        
        hide jasmine
        
        p "Please have your conversation with your friend when the lesson isn't ongoing, Stones. [rg]?"
        
        "The facepalming guy next to Jasmine speaks up."
        
        show roger casual frown at right
        
        rg "Present..."
        
        hide roger
        
        p "The same instructions to you as well, Gale."
        
        p "And last but not least, [als]."
        
        "A younger man" "Here."
        
        "Patrick nods."
        
        p "Good. I can't promise I'll remember all the names correctly by the end of the lesson, but I'll try. First, how about we all tell how we ended up here?"
        
        p "I'll go first. I mean, I am here because that's what my work agreement told me to do."
        
        p "Heh. Humor aside, I ended up becoming a German teacher after I spent time as an exchange student in Switzerland."
        
        p "I was already studying to become a language teacher, but at the time I was majoring in Latin. I ended up finding a truer passion for German, however, and now I am here."
        
        p "That's my story. Who wants to go next?"
        
        "..."
        
        jj "I can go next. I retired recently and now I finally have some time to study languages. I have wanted to study German for years."
        
        er "I'm heading to Austria for a business trip, to I need some understanding of German."
        
        sl "I'm going on the same trip as Eileen. I did study German in school, but it's been years and I've forgotten everything, so I decided to come with."
        
        show jasmine casual up smile at right
        
        js "I've been really itching to learn some German to talk with some of my friends online and I decided that now's the best time to do that!"
        
        js "Now's better than tomorrow, right, Roger?"
        
        show roger casual frown at middle
        
        rg "Yeah..."
        
        rg "*sigh* Honestly, my reason to be here is that Jasmine dragged me along."
        
        p "Well, I hope that you'll get a good learning experience nevertheless." 
        hide jasmine
        hide roger
        
        menu:
            p "What about you, [last_name]?"
            
            "I saw an ad about it at the local café and got interested":
                p "Oh, that's very nice. Good to know that the ads did do something."
                
                als "I came because of the ads too."
            "I wanted to start learning German.":
                als "Same here."
            
            "I want to make more friends.":
                p "Then you have come to the right place. Language courses like this are perfect for getting to know people and forming friendships!"
                
                als "I want to make some new friends too."
                
        p "Very well. [iv], what about you?"
        
        "[ivm] rolls her eyes again."
        
        show ivy side casual frown at right
        
        ivm "Because my dad told me to."
        
        "Patrick chuckles."
        
        p "I see you're not motivated. Still, I'm sure that this course will be useful for you."
        
        ivm "Sure, whatever..."
        
        hide ivy
        
        p "Well then, now that the introductions are done, I'll tell you about how this course works..."
        
        jump outside
    $ lesson = lesson+1

label outside:
    
    if lesson == 1:
        
        scene school_hallway_day
        
        "Your head is filled with information on what the course consists of and the tests and homework you will need to do to pass."
        
        "This had better be worth it."
        
        "You see [rg] and [js] talking with one another. You take a few steps towards them, hoping you could talk to them, but their conversation seems to turn into an argument."
        
        "It's probably for the best not to get involved. You turn back and head home. Perhaps you'll have better luck with the next lesson when everything is supposed to truly kick off..."
        
        # TODO Restructure this into different files
                
                
        
        
        
    return
