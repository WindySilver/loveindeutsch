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
        
        "[p] nods."
        
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
        
        show roger casual frown at center
        
        rg "Yeah..."
        
        rg "*sigh* Honestly, my reason to be here is that Jasmine dragged me along."
        
        p "Well, I hope that you'll get a good learning experience nevertheless." 
        hide jasmine
        hide roger
        
        menu:
            p "What about you, [last_name]?"
            
            "I saw an ad about it at the local café and got interested.":
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
        
        "[p] chuckles."
        
        p "I see you're not motivated. Still, I'm sure that this course will be useful for you."
        
        ivm "Sure, whatever..."
        
        hide ivy
        
        p "Well then, now that the introductions are done, I'll tell you about how this course works..."
        
    if lesson == 1:

        p "Guten Abend. That's German for \"Good evening\". Today, we will cover greetings and the numbers from 0 to 10."

        p "First, greetings. Like I said earlier, \"guten Abend\" means \"good evening\". To say \"good afternoon\", you say \"guten Tag\"."

        menu:
            "You realize that maybe you should take notes, if only to help with revising things later on."

            "You'll take notes.":
                "You take out your pencil and notebook and start writing things down."
                $ notes[1] = True
            "Nah, you'll be fine with just the material.":
                "You decide not to take notes and simply listen to the teacher."

        p "\"Hello\", on the other hand, is easier to remember. It's \"hallo\"."

        p "There are other ways to say hello, of course, depending on the area. For example, \"grüezi\" is a Swiss German way to say hello, while in Austria you might be greeted with \"Grüß Gott\"."

        p "If you want to say \"goodbye\" in German, you can say \"auf Wiedersehen\"."

        p "We will discuss greetings and goodbyes in greater detail on a later lesson. Now, let's move on to numbers."

        "The slide changes to show a list of numbers."

        p "Let's count from zero. Repeat after me: null."

        e "Null."

        p "Eins."

        e "Eins."

        p "Zwei."

        e "Zwei."

        p "Drei."

        e "Drei."

        "You overhear [js] whisper to her friend between the numbers behind your back."

        show jasmine casual up smile

        js "Polizei."

        "You hear [rg] snort. The teacher gives the duo a look, so you don't turn around to look at them. Then the counting continues as if nothing had happened."

        hide jasmine

        p "Vier."

        e "Vier."

        p "Fünf."

        e "Fünf."

        p "Sechs."

        e "Sechs."

        p "Sieben."

        e "Sieben."

        p "Acht."

        e "Acht."

        p "Neun."

        e "Neun."

        p "Zehn."

        e "Zehn."

        p "Excellent work, everyone. Next, let's get up from the chairs and talk. I want you all to talk to your fellow students at random and have a following discussion: greeting, telling a number of your choice and saying goodbye."

        p "To say \"My number is\", say \"Meine Nummer ist\"."

        "The room is filled with the sound of scraping chairs. You try to figure out who to talk with. The first one you make eye contact is [rg]. You walk up to him."

        show roger casual frown

        rg "Hello. I-I mean hallo. Uh, meine Nummer ist..."

        rg "Um... null..."

        y "Hallo. Meine Nummer ist... Er..."

        python:
            numbers_right = ["null", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn"]
            numbers_wrong = ["noll", "einz", "swei", "trei", "viir", "funf", "zechs", "seben", "aht", "nein", "sehn"]
            chosen_number = renpy.random.randint(0, 10)
            wrong = numbers_wrong[chosen_number]
            correct = numbers_right[chosen_number]

        "You realize that you did not even think of a number, so you pick the first one that comes to your mind... [chosen_number]!"

        menu:
            y "Meine Nummer ist..."

            "[wrong]":
                rg "Uh... Wasn't it... Nevermind. Auf Wiedersehen."
            "[correct]":
                rg "Auf Wiedersehen."
            "zwala":
                $ roger_approve -= 1
                "[rg] frowns at you."
                rg "I'm pretty sure that's not a number, at least not one we just learned."
                y "Oh."
                "That definitely did not go well."
                rg "Auf Wiedersehen."
        
        y "Auf Wiedersehen."

        hide roger

        "You turn to look at other people. Your eyes meet [sl]'s."

        sl "Hallo! Meine Nummer ist drei."

        menu:
            y "Hallo. Meine Nummer ist..."

            "[wrong]":
                sl "Hmm. I think it was [correct]. Auf Wiedersehen."
                y "Auf Wiedersehen."
            "[correct]":
                sl "Auf Weidersehen."
            "zwala":
                "[sl] frowns at you."
                sl "Are you even trying?"
                y "Huh?"
                sl "That isn't a German number. You should take notes during the lesson and check them when you don't know the answer rather than coming up with nonsense, you know."
                "Whoops."
                y "Oh..."
                sl "Auf Wiedersehen."

        y "Auf Wiedersehen."

        "Before you managed to make eye contact with someone else, the lesson was over. You headed outside, hoping that this time you could find someone to talk with."

        

        


    $ lesson = lesson+1
    jump outside