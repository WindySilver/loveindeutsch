label ivy_abandons:
    $ ivy_abandon = True
            
    ivm "You're not trying at all, are you? Why did you even enroll on the course?"

    y "I, uh, I... Well, I wanted to make new friends."

    ivm "Well, you definitely aren't working for it. I'm not here to chat or make friends, I'm here because I have to."

    ivm "The fact that you're here voluntarily and are messing around pisses me off."

    y "Sorry..."

    return

label roger_abandons:
    $ roger_abandon = True
            
    rg "Look, this isn't working out."

    y "Huh?"

    rg "[j] dragged me to the German course, so I'd better at least put enough effort to get through it. You clearly aren't."
    
    rg "I've been dragged down by bad influences too many times in my life already to keep any around. I'm sorry, I really am, but I have to cut you out."

    rg "You seem really nice and in other circumstances we could've been good friends, but I can't afford to lose my grip on this course."

    rg "I should get going. Goodbye, [full_name]."

    return

label jasmine_abandons:
    $ jasmine_abandon = True
            
    "[js] sighs."

    js "Look, I've given you the benefit of the doubt. [r] sometimes loses his focus on stuff and needs someone to knock some sense into him. I figured you might be the same."

    js "But you aren't trying at all, are you? You aren't trying to learn anything. You're just trying to get friends and have fun."

    js "I'm not here for that. I'm on this course to learn. If you can't put in even the slightest effort to do that, then we won't work out."

    y "Sorry. I... I guess I got carried away or something."

    js "I suppose. In any case, I'm done. See you on the remaining lessons... if you even bother to show anymore."

    return

label jasmine_friended:

    j "You know, you said that you came on the German course to get friends."

    y "Yeah. What about that?"

    j "Well, you seem cool to hang out with. How about you and I be friends?"

    y "Sure!"

    "Score! While [j] doesn't go to your school, having a friend to hang out with outside school would be great."

    return

label roger_friended:

    r "Um... You know, I've been thinking..."

    y "About what?"

    r "Well, [n] has kept saying that you're cool and all and I could use some more friends..."

    r "And, um, now that I've gotten to know you a bit, um..."

    return

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

    iv "So..."

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

    return


