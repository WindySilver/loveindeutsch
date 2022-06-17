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

            "Take notes":
                "You take out your pencil and notebook and start writing things down."
                $ notes[1] = True
            "Nah, you'll be fine with just the material.":
                "You decide not to take notes and simply listen to the teacher."

        p "\"Hello\", on the other hand, is easier to remember. It's \"hallo\"."

        menu:
            "Let me check my notes":
                $renpy.call_screen("notes")

        p "There are other ways to say hello, of course, depending on the area."
    $ lesson = lesson+1
    jump outside