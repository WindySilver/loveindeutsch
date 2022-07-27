label ivy_studying:
    if lesson == 3:
                
        "You meet [iv] at the cafe at 18.30."
        show ivy side casual frown
        y "Hi."
        iv "Hi."
        iv "Let's get this stuff over with."
        "Without any more words, you two got into working on the homework."
        menu:
            iv "\"My name is...\" and \"I am\". You remember the differences, right?"
            "Nope.":
                $ ivy_approve -= 2
                iv "..."
                iv "When are you going to say \"just kidding\"?"
                y "Um... I'm not?"
                iv "You've got to be kidding me..."
                if ivy_approve <= abandon_level and not ivy_abandon:
                    call ivy_abandons
                    iv "I think we're done here."
                    "[iv] leaves you alone at the cafe. You are fairly certain that you hear snickering directed towards you but you ignore it to finish your homework alone."
                    "You eventually get the homework done and head back home. Hopefully the next lesson would go better."
            "They use different verbs. Ist and heiße.":
                iv "Pretty much. The basic forms for the verbs are \"sein\" and \"heißen\", and when used with \"I\" \"sein\" is \"bin\"."
                y "So, \"ich heiße...\" and \"ich bin\"?"
                iv "Exactly."
            "They use different verbs. Sein and heißen.":
                $ ivy_approve += 1
                iv "Correct. You remember the conjugations?"
                y "Yup. \"Ich heiße\" and \"ich bin\"."
                iv "Indeed."

                show ivy side casual smile
                iv "Huh. You actually seem to be taking this stuff seriously."
        
        iv "Moving on..."
        "You finish the homework in record time thanks to [iv]."
        iv "Well, we're done now. I must say, I'm impressed with you."
        y "Thanks."
        if ivy_approve >= ivy_approve_friend_low and not ivy_friend:
            iv "..."
            call ivy_friended
        
        iv "We should call it a day now. See you at school. Or the next lesson."
        "With that, you both leave the cafe. You do not run into each other at school on the following days, instead only meeting when the next lesson starts."
        jump classroom

    if lesson == 4:

        "You meet [iv] at the cafe in the afternoon, as agreed yesterday."
        if ivy_friend:
            show ivy side casual smile
        else:
            show ivy side casual frown
        y "Hi."
        iv "Hi. Shall we get to the homework right away?"
        y "Yeah, let's do that."
        iv "Alright then. Apparently there's a bit about both goodbyes and greetings. Let's tackle the greetings first."
        iv "The greeting we have covered during the lesson was \"good morning\", that was \"guten Morgen\". Do you remember the ones from the first lesson?"
        y "I do."
        iv "Good. Then this'll be a breeze."
        y "Yup. At least this is easy."
        iv "I suppose. A bit of a challenge would be nice though."
        "You finish the exercise on greetings swiftly and move on to goodbyes."
        iv "The only goodbyes we've covered are \"auf Wiedersehen\" and \"tschüss\", so there isn't much to do here. The former is \"goodbye\" and the latter is \"bye\"."
        iv "Oh, and there's also \"good night\". That's a part of this exercise too."
        menu:
            iv "Do you remember what \"good night\" is in German?"
            "No idea.":
                $ ivy_approve -= 2
                show ivy side casual frown
                iv "Of course..."
                iv "It's \"gute Nacht\"."
                y "Oh. Right."
                if ivy_approve <= abandon_level:
                    call ivy_abandons
                    iv "I think we're done here."
                    "[iv] leaves you alone at the cafe. You are fairly certain that you hear snickering directed towards you but you ignore it to finish your homework alone."
                    "You eventually get the homework done and head back home. Hopefully the next lesson would go better."
                    jump classroom
            "Gute Night":
                show ivy side casual frown
                iv "Har har. Now be serious, will you."
                iv "It's \"gute Nacht\"."
                y "I know."
                "If Tamera was there, she would say \"no you did not\". Fortunately, she was not there (at least not within hearing distance)."
                iv "Good. Now let's remain serious. I'm not here to fool around."
            "Gute Nacht":
                $ ivy_approve += 1

                iv "Indeed."

        iv "Moving on..."
        "You finish the exercise in record time thanks to [iv]'s understanding of the material."
        show ivy side casual smile
        iv "Huh. That went actually well."
        if ivy_friend and ivy_approve >= ivy_approve_romance_low:
            iv "Before we head out, there's something... something I'd like to ask of you. Do you have the time?"
            y "Of course. I don't have any other plans than this meeting for today."
            show ivy side casual frown
            iv "Good. Good."
            call ivy_romanced
        elif ivy_approve >= ivy_approve_friend_low and not ivy_friend:
            iv "Before we finish for the day, there's something I'd like to talk about. Do you have some time?"
            y "Sure. I don't have any other plans than this meeting for today."
            iv "Good."
            call ivy_friended
        iv "Alright. Time for me to head out. See you on the next lesson. And... thank you for this meeting."
        y "No, thank you. See you on the next lesson."
        "You go on your separate ways."
        jump classroom
    return
    
        
label jasmine_roger_studying:
    if lesson == 3:    
        "You meet [j] and [r] at the cafe at 16.00."
        show jasmine casual up smile at left
        show roger casual smile at right
        j "Hi!"
        r "Hi there."
        y "Hi."
        j "So, let's get started, shall we?"
        y "Sure."
        "You start working on the homework once you have your drinks."
        menu:
            r "\"My name is...\" and \"I am\". [first_name], do you remember the differences?"
            "Nope.":
                $ roger_approve -= 1
                $ jasmine_approve -= 1
                show roger casual frown
                r "..."
                r "Um... Alright..."
                j "\"My name is\" uses the verb \"heißen\" while \"I am\" uses \"sein\"."
                r "Right."
            "They use different verbs. Ist and heiße.":
                j "Basically. The basic forms for the verbs are \"sein\" and \"heißen\", and when used with \"I\" \"sein\" is \"bin\"."
                y "So, \"ich heiße...\" and \"ich bin\"?"
                j "Precisely."
            "They use different verbs. Sein and heißen.":
                $ roger_approve += 1
                $ jasmine_approve += 1
                j "Yup! Do you remember the conjugations for them too?"
                y "Yup. \"Ich heiße\" and \"ich bin\"."
                r "Oh, right, those were it. Thanks."
        
        j "Alright, so, the next task is..."
        "You finish the homework in record time thanks to [j] and [r]."
        j "Aaand that's done! Woo!"
        j "I'll be right back. Gotta use the toilet."
        hide jasmine
        if roger_approve >= roger_approve_friend_low and not roger_friend:
            r "That went surprisingly well."
            r "..."
            call roger_friended
        else:
            
            r "Well, that went well."
            r "You feel you're starting to get a grip on this yet?"
            y "I think I am."
            r "That's nice."
        show jasmine casual up smile
        j "Aaand I'm back! You ready to head out?"
        y "Yeah."
        if roger_approve <= abandon_level and not roger_abandon:
            r "Yeah. I just need to exchange a few words with [first_name] first. You go on ahead."
            j "Got it. See you outside."
            hide jasmine
            show roger casual frown
            call roger_abandons
            "[r] leaves. You stay behind, figuring that you probably should let him and [j] head out first."
            "You are definitely messing things up. You should probably pay more attention at the next lesson before even [j] decides that you're not good company."
            jump classroom
        
        else:
            r "Yeah, I'm ready to go."
            j "Great. Let's go then."
            jump walk_home
    return



label roger_studying:
    if lesson == 4:
        "You meet [r] at the cafe in the evening, as agreed yesterday."
        show roger casual smile
        r "Hi there."
        y "Hi."
        r "Thanks for coming. Shall we get right into the homework?"
        y "Sure."
        r "Alright then. It seems like there's a bit about both goodbyes and greetings. Let's tackle the greetings first, shall we?"
        y "Sounds good to me."
        r "Good. The greeting we covered during the lesson was \"good morning\", that was \"guten Morgen\", I think. We had greetings on the first lesson, too."
        r "We should be fine, right?"
        y "Yeah."
        r "Let's get to it then."
        "You start working on the exercise on greetings and finish it swiftly before moving on to goodbyes."
        r "I think the only goodbyes we've covered are \"auf Wiedersehen\" and \"tschüss\", so there isn't much to do here. The former is \"goodbye\" and the latter is \"bye\"."
        iv "Oh, right, and there's also \"good night\". I always forget it's a goodbye."
        
        show roger casual frown
        menu:
            
            r "What was \"good night\" is in German again?"
            "No idea.":
                $ roger_approve -= 1
                r "Ah... Well, let me check my notes."
                r "It's \"gute Nacht\"."
                y "Oh. Right."
                if roger_approve <= abandon_level:
                    call roger_abandons
                    "[r] leaves you alone at the cafe. You are fairly certain that someone in the neighbouring table is talking about you but you ignore it in favor of finishing your homework."
                    "You eventually get the homework done and head back home. Hopefully the next lesson would go better."
                    jump classroom
            "Gute Night":
                show roger casual smile
                r "Haha, that's funny."
                r "Jokes aside, it's \"gute Nacht\"."
                y "I know."
                "If Tamera was there, she would say \"no you did not\". Fortunately, she was not there (at least not within hearing distance)."
                r "I figured that you knew."
            "Gute Nacht":
                show roger casual smile
                $ roger_approve += 1
                
                r "That's correct."
                
        r "Well then, let's move on."
        "You finish the exercise in record time thanks to [r]'s help."
        show roger casual smile
        r "Ah, good. We're done with the homework."
        if roger_friend and roger_approve >= roger_approve_romance_low:
            show roger casual frown
            r "Um... are you in a hurry to go back home?"
            y "No. I've still got plenty of time before I need to get back home."
            r "O-okay... That's... that's good.."
            r "I... I think there's something I should talk about with you."
            y "Okay."
            call roger_romanced
        elif roger_approve >= roger_approve_friend_low and not roger_friend:
            show roger casual frown
            r "Um... are you in a hurry to go back home?"
            y "No. I've still got time before I need to leave."
            r "Ah, good... I'd like to hang out for a bit... I could use some company since [n] is at work."
            y "[n]?"
            r "Oh, right, you don't know. That's [j]'s nickname, although I don't think anyone except me uses it."
            y "Oh, okay."
            y "Well, I do have time to hang out if you want to hang out with me."
            show roger casual smile
            r "I'm glad to hear that. I... I'd like to talk with you a bit more, after all..."
            call roger_friended
        r "I guess we should get going. Thanks for today."
        y "No, thank you. See you on the next lesson."
        "You go on your separate ways."
        jump classroom
    return

label jasmine_studying:
    if lesson == 4:
        "You meet [j] at the cafe in the evening, as agreed on the day before yesterday."
        show jasmine casual up smile
        j "Hii!"
        y "Hi."
        j "Thanks for making the time to do the homework with me."
        
        y "No problem."
        
        j "Well, let's get straight into work, shall we?"
        y "Sure."
        j "So, there's exercises on both goodbyes and greetings. How about we tackle the greetings first?"
        y "Sounds good to me."
        j "Great! The greeting we covered during the lesson was \"good morning\", which is \"guten Morgen\". That goes on top of the greetings from the first lesson."
        j "We've definitely got this, don't you think?"
        y "Definitely."
        j "I was hoping you'd say that."
        "You start working on the exercise on greetings and finish it swiftly before moving on to goodbyes."
        j "Now, to the goodbyes... We've covered \"auf Wiedersehen\", which is \"goodbye\", and  \"tschüss\", which is \"bye\", and also the phrase for \"good night\"."
        menu:
            j "Do you remember what's \"good night\" in German?"
            "No idea.":
                $ jasmine_approve -= 1
                show jasmine casual up frown
                j "Oh... Well, it's \"gute Nacht\"."
                y "Oh. Right."
                if jasmine_approve <= abandon_level:
                    call jasmine_abandons
                    "[j] leaves you alone at the cafe. You are fairly certain that the laughter coming from the neighbouring table is aimed at you but you ignore it in favor of finishing your homework."
                    "You eventually get the homework done and head back home. Hopefully the next lesson would go better."
                    jump classroom
            "Gute Night":
                "[j] snorts."
                j "I can't believe you got something like a laugh out of me with a bad joke like that."
                j "Anyhoo, it's \"gute Nacht\"."
                y "I know."
                "If Tamera was there, she would say \"no you did not\". Fortunately, she was not there (at least not within hearing distance)."
                j "Just as I expected."
            "Gute Nacht":
                $ jasmine_approve += 1
                
                j "Yup. That's the phrase."
                
        j "Let's take on that exercise then!"
        "You finish the exercise in record time thanks to [j]'s help."
        show jasmine casual up smile
        j "And that's done!"
        if jasmine_friend and jasmine_approve >= jasmine_approve_romance_low:
            j "I know it's getting a bit late, but would you mind sticking around for a bit?"
            y "I don't mind. Is there something on your mind?"
            j "Yes, there is."
            call jasmine_romanced
        elif jasmine_approve >= jasmine_approve_friend_low and not jasmine_friend:
            j "I know it's getting a bit late, but would you mind staying for a bit?"
            y "I don't mind. Do you want to talk about something?"
            j "I do."
            call jasmine_friended
        j "Again, thanks for coming today."
        y "No, thank you. Shall we walk home together?"
        j "Sounds good to me."
        "You head out into the evening."
        jump walk_home
    return

label alone:
    if lesson == 3:

        "You do all the homework, including your German homework, alone in the evening. It's lonely work and you wonder if you should have studied with [iv] so that she would not have had to do the same work alone."

        "Honestly, studying alone was lame after the group homework session at the cafe. You should probably do your homework with the others when you can."
        
    if lesson == 4:

        "You do all the homework, including your German homework, alone in the evening. It's lonely work and you wonder if you should have studied with someone else to give your studying a bit of a boost, to motivation if nowhere else."

        "Honestly, studying alone was lame after the group homework session at the cafe. You should probably do your homework with the others when you can."
        
    return
    
label skip_studying:
    if lesson == 3:

        "Once you were done with your other homework, you glanced at your German homework. The memory of the others' looks when you said that you'd skip doing it stung and you did consider doing the homework after all for a moment."
            
        "However, you were still confident you had learned the lesson's contents, so you left the homework undone."

    if lesson == 4:

        "Once you were done with your other homework, you glanced at your German homework. The memory of the others' looks when you said that you'd skip doing it stung and you did consider doing the homework after all for a moment."
            
        "However, you were still confident you had learned the lesson's contents, so you left the homework undone."

    return

label plans:
    if lesson == 3:

        "Once you were done with your other homework, you glanced at your German homework. Since you had plans to do it tomorrow, you left it be."

    if lesson == 4:

        "Once you were done with your other homework, you glanced at your German homework. Since you had plans to do it tomorrow, you left it be."

    return
