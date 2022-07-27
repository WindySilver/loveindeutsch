label ivy_abandons:

    play music "audio/The Puzzle Loop.ogg" loop

    python:
        ivy_abandon = True
        ivy_friend = False
        ivy_romance = False
            
    ivm "You're not trying at all, are you? Why did you even enroll on the course?"

    y "I, uh, I... Well, I wanted to make new friends."

    ivm "Well, you definitely aren't working for it. I'm not here to chat or make friends, I'm here because I have to."

    ivm "The fact that you're here voluntarily and are messing around pisses me off."

    y "Sorry..."

    return

label roger_abandons:

    play music "audio/The Puzzle Loop.ogg" loop
    
    python:
        roger_abandon = True
        roger_friend = False
        roger_romance = False
            
    rg "Look, this isn't working out."

    y "Huh?"

    rg "[j] dragged me to the German course, so I'd better at least put enough effort to get through it. You clearly aren't."
    
    rg "I've been dragged down by bad influences too many times in my life already to keep any around. I'm sorry, I really am, but I have to cut you out."

    rg "You seem really nice and in other circumstances we could've been good friends, but I can't afford to lose my grip on this course."

    rg "I should get going. Goodbye, [full_name]."

    return

label jasmine_abandons:

    play music "audio/The Puzzle Loop.ogg" loop
    
    python:
        jasmine_abandon = True
        jasmine_friend = False
        jasmine_romance = False
            
    "[js] sighs."

    js "Look, I've given you the benefit of the doubt. [r] sometimes loses his focus on stuff and needs someone to knock some sense into him. I figured you might be the same."

    js "But you aren't trying at all, are you? You aren't trying to learn anything. You're just trying to get friends and have fun."

    js "I'm not here for that. I'm on this course to learn. If you can't put in even the slightest effort to do that, then we won't work out."

    y "Sorry. I... I guess I got carried away or something."

    js "I suppose. In any case, I'm done. See you on the remaining lessons... if you even bother to show anymore."

    return

label jasmine_friended:

    play music "audio/Mazit Music Loop.ogg" loop
    
    python:
        jasmine_abandon = False
        jasmine_friend = True
        jasmine_romance = False

    j "You know, you said that you came on the German course to get friends."

    y "Yeah. What about that?"

    j "Well, you seem cool to hang out with. How about you and I be friends?"

    y "Sure!"

    "Score! While [j] doesn't go to your school, having a friend to hang out with outside school would be great."

    return

label roger_friended:

    play music "audio/Mazit Music Loop.ogg" loop    

    show roger casual smile

    python:
        roger_abandon = False
        roger_friend = True
        roger_romance = False

    r "Um... You know, I've been thinking..."

    y "About what?"

    r "Well, [n] has kept saying that you're cool and all and I could use some more friends..."

    r "And, um, now that I've gotten to know you a bit, um..."

    show roger casual frown

    r "Nevermind. Forget that I said anything."

    y "Do you want to be my friend?"

    r "Oh, um, well..."

    show roger casual frown blush

    r "Well, yeah... If [n] thinks you could be good company for me, then yeah..."

    show roger casual open blush

    r "I-if that's fine with you, of course!"

    y "Of course it is! I took the German course to get friends, after all. Besides, you're cool too."

    r "Really? You're just saying, right?"

    r "Right?!"

    y "I'm not."

    show roger casual frown blush

    r "O-okay then... Well... Okay."

    show roger casual smile blush

    r "Let's be friends then."

    y "Let's be friends."

    "The awkwardness aside, you feel like you're getting somewhere with making new friends. Awesome!"

    "Now, if only you could befriend [iv] so that you'd have someone to hang out with at school..."

    "That's going to be a challenge, considering how cold and distant she is."

    return

label ivy_friended:

    play music "audio/Mazit Music Loop.ogg" loop    

    python:
        ivy_abandon = False
        ivy_friend = True
        ivy_romance = False

    iv "There's something I want to say. Don't interrupt me, okay?"

    y "Okay."

    iv "Good."

    iv "At first, I thought that you'd be just yet another guy who'd do nothing but waste my time on useless stuff. You wouldn't have been the first nor the last."

    iv "But... you {i}are{/i} dedicated to the course. Even though your motives are definitely in getting friends rather than learning German."

    iv "Dad and Uncle Patrick keep telling me that I should make some friends outside of Judo and... well..."

    iv "I'm only going to ask once."

    iv "Will you be that friend that they want me to make?"

    "Bingo!"

    y "I'd love to!"

    show ivy side casual smile

    iv "I figured as much. Let's be friends then."

    y "Can we hang out at school?"

    iv "What, that rowdy friend of yours isn't enough?"

    y "She doesn't hang out with me much anymore, so yeah."

    iv "Ah. I see how it is."

    iv "Well, we shall hang out at school. It might do us both good... at least if Dad is to believed."

    "You suddenly realize that this is the first time you have ever seen [iv] smile."

    "Major success!"

    return

label ivy_romanced:

    play music "audio/LandingPage Loop.ogg" loop

    python:
        ivy_abandon = False
        ivy_friend = False
        ivy_romance = True

    iv "So, well, the thing is..."

    iv "I'm not the kind of person to fall for anyone. At least I think I don't have a type."

    iv "But... well..."

    iv "It turns out that I did fall for someone."

    iv "I don't know how or when but I fell for you."

    menu:

        iv "So, the thing I want to ask is... do you feel the same?"

        "I do, actually.":
            show ivy side casual frown blush

            iv "Oh. I... I see. Well... if we feel the same way, then... shall we... become a thing?"

            y "I'd love that."

            show ivy side casual smile

            iv "Alright. Then... then we'll be a couple from now on, I guess."

            "Score!!!"

            y "Indeed."

        "I'm sorry, but I don't.":
            $ ivy_reject = True

            iv "Oh. I see."

            show ivy side casual smile

            iv "Well.. that does actually make things easier. I don't have to figure out how to slot a partner into my life this way."

            iv "Thank you for being honest with me."

            y "No problem. Can we stay friends?"

            iv "Of course. I wouldn't have it any other way."

            "Even though you just rejected someone, you feel strangely good about it. How strange."

            "Perhaps it was just that you were honest with yourself - you could not see a future with [iv] as your girlfriend, after all."

    iv "Well, that was all I had to say about this topic."

    return

label roger_romanced:

    play music "audio/LandingPage Loop.ogg" loop


    python:
        roger_abandon = False
        roger_friend = False
        roger_romance = True

    r "So, um, well..."

    show roger casual frown blush

    r "Uh..."

    y "Take your time."

    r "Thanks. Um..."

    r "Eh, best just to rip the bandaid off."

    r "I'm in love with you, [first_name]."

    "...Oh."

    r "There. I... I said it. Phew..."

    r "And [n] said that it wouldn't be so difficult..."

    menu:

        r "So, uh, now that you know... What... do you think?"

        "I'm in love with you too.":
            
            show roger casual open blush

            r "Really? As in, you... you mean it?"

            y "Uh-huh."

            r "Wow..."

            r "I... I always thought that it was one-sided..."

            r "Well, um, since... we both feel that way... um... how about..."

            r "How about we become a couple? Go on dates and... so on...?"

            y "I'd love to."

            show roger casual smile blush

            r "Then it's settled. I... Thank you, [first_name]. Thank you."

            "Score!!"

        "I'm sorry, but I don't feel the same way.":

            $ roger_reject = True

            r "Ah. I... I actually had a feeling you might say that."

            r "Well, that's... that's fine. I understand."

            r "Um... can we still stay friends, though? I really like spending time with you."

            y "Naturally."

            show roger casual smile blush

            r "I'm glad. Thank you... And thanks for being honest with me rather than stringing me along."

            y "No problem."

            "Even though you just rejected someone, you feel strangely good about it. How strange."

            "Perhaps it was just that you were honest with yourself - you could not see a future with [r] as your boyfriend, after all."

    r "That's all I wanted to talk about."

    return


label jasmine_romanced:

    play music "audio/LandingPage Loop.ogg" loop


    python:
        jasmine_abandon = False
        jasmine_friend = False
        jasmine_romance = True

    j "I'm going to be blunt here. I have a crush on you."

    "You blink. That was... very fast."

    show jasmine casual up frown

    menu:

        j "Do you happen to feel the same towards me?"

        "Actually, I do.":

            show jasmine casual up smile

            j "I'm glad to hear that."

            j "In that case, how about you and I become a couple?"

            y "I'd love that."

            j "Great!"

            j "Then you get the ultra-rare privilege of calling me [n]."

            j "The only other person who gets to call me that is [r]."

            y "Wow. Thank you."

            j "No problem. Thanks for agreeing to be with me."

        "I'm sorry, I don't.":

            $ jasmine_reject = True

            j "I see... Very well. That cannot be forced."

            show jasmine casual up smile

            j "Thanks for being honest with me. I'd very much rather have a rejection than strung along, after all."

            j "Still, I hope that this doesn't change our friendship."

            y "Don't worry, this doesn't change it."

            j "Good."

            "Even though you just rejected someone, you feel strangely good about it. How strange."

            "Perhaps it was just that you were honest with yourself - you could not see a future with [j] as your partner, after all."
        
    j "That's all I wanted to talk to you about."

    return
