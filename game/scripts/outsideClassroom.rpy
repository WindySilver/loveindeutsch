label outside:

    play music "audio/Calm Loop.ogg" loop if_changed
    
    if lesson == 1:
        
        scene school_hallway_day
        
        "Your head is filled with information on what the course consists of and the tests and homework you will need to do to pass."
        
        "This had better be worth it."
        
        "You see [rg] and [js] talking with one another. You take a few steps towards them, hoping you could talk to them, but their conversation seems to turn into an argument."
        
        "It's probably for the best not to get involved. You turn back and head home. Perhaps you'll have better luck with the next lesson when everything is supposed to truly kick off..."
        
        jump home

    if lesson == 2:
        
        scene school_hallway_day

        "You look around, hoping to spot familiar faces. To your surprise, you see [ivm] talking with [rg] and [js]. Or maybe it's the other way around."

        "Anyhow, you figure this might be a good time to try and talk with them."

        show jasmine casual up smile at right

        show ivy side casual frown at left

        show roger casual frown at center

        y "Uh, hi."

        if roger_approve < roger_approve_neutral_low:
            rg "...Hi."
            
            show jasmine casual up frown
            
            js "That the one you mentioned?"
            
            rg "Yeah..."

            "You can't help but feel that they are referring to how you messed up during the lesson."

            js "Well, hi. [full_name], was it?"

            y "Uh, yeah, that's me."

            show jasmine casual up smile

            js "I'm [js]. This guy here is my friend, [rg]."

            rg "I can introduce myself by myself, y'know."
            
            js "I know. I figured I'd do it for you anyway."

            ivm "Are we done?"
  
        else:
            show roger casual smile
            
            rg "Oh, hi. [full_name], was it?"
            
            y "Yeah, that's me."

            "You are certain that this is the first time you've seen [rg] smile."

            js "Hi! I'm [js]. This Shy Guy here is [rg]."

            rg "Hey, I can introduce myself by myself!"

            js "Heh, I know. I figured I'd save us all some minutes by doing it for you."

            ivm "Are done here yet?"


        js "Nope. You haven't introduced yourself yet."

        ivm "[ivm]."

        y "Pleasure to meet you all."

        js "Say, how about the four of us tackle our homework together?"

        ivm "I don't have time today. Got practice to head out to."

        js "Then how about tomorrow after school? We could meet up at the nearby café. How does 18.30 sound like?"

        y "Fine by me."

        rg "Sure."

        ivm "Will you all get off my case if I say yes?"

        js "Perhaps."

        ivm "Sure, whatever. Let's meet then."

        js "Great! See you all tomorrow!"

        jump home

    if lesson == 3:

        scene school_hallway_day

        show jasmine casual up smile at center

        show ivy side casual frown:
            flip
            right

        show roger casual smile at left

        j "I gotta go to work, so I can't hang around for long. Can we meet up tomorrow, maybe around 16?"

        iv "I can't make it. Anything between 18 and 20 works tomorrow."

        show roger casual frown

        r "I can't make it after 19."

        show jasmine casual up frown

        j "What about the day after tomorrow?"

        y "I can't make it then. I'll be visiting my grandparents for most of the day."

        j "Okay. Then we gotta do homework in smaller groups. [r], you got time tomorrow?"

        show roger casual smile

        r "Yeah."

        show jasmine casual up smile

        j "Then we'll study together. What about you, [first_name]?"

        menu:

            "This would be an excellent way to get to know [j] and [r] more. Then again, you could perhaps get through to [iv] too if you studied with her."

            "[iv]" if not ivy_abandon:
                
                call all_approve

                y "I'll study with you, [iv]. If it's fine with you."

                iv "Sure, whatever."

                j "Then it's settled. We'll see on the next lesson then. Bye now!"
                $ ivy_approve += 1
                $ study = "i"
            
            "[j] and [r]":
                call all_approve

                y "I'll study with you two if you'll have me."

                j "Of course we will! Welcome aboard!"

                r "Shall we see each other at the cafe at 16?"

                j "Sounds good to me."

                y "Agreed."

                j "Good. Now, I gotta jet. See you!"

                python:
                    roger_approve += 1
                    jasmine_approve += 1
                    study = "rj"

            "I'll study by myself.":
                call all_approve

                j "Alright. Then we'll see each other at the next lesson. Bye now!"
                $ study = "y"

            "I'll skip homework.":
                jump all_disapprove

                show jasmine casual up frown
                show roger casual frown

                if ivy_approve <= abandon_level and not ivy_abandon:
                    jump ivy_abandons
                    call all_disapprove

                j "Seriously? Skip homework?"

                y "Today's stuff was easy. I'll be fine."

                j "Well-"

                iv "It's your funeral."

                j "Eh... I mean, I don't recommend skipping homework even if you feel you learned it all in one go, but you do you I guess."

                j "Anyhoo, I gotta go now. See you at the next lesson."

                $ study = "skip"

        "With that, [j] left with [iv] following suit fast."

        hide jasmine
        hide ivy

        if roger_approve <= abandon_level:
            jump roger_abandons
            $ jasmine_approve -= 1

        elif roger_approve >= roger_approve_friend_low:

            show roger casual frown

            r "Do you have time to hang out now? I could use some company since [n] is at work."

            y "[n]?"

            r "Oh, right, you don't know. That's [j]'s nickname, although I don't think anyone except I use it."

            y "Oh, okay."

            y "I have time to hang out if you want to hang out with me."

            show roger casual smile

            r "I'm glad to hear that. Come, let's head out."

            scene city_afternoon

            jump roger_friended

        jump home

        if lesson == 4:

            hide patrick

            "Once you got your items back, you gathered together with [j], [r] and [iv]."

            show jasmine casual up frown at center
            show ivy side casual frown at left
            show roger casual frown at right

            j "Well, that sucked big time."

            y "Very much."

            r "I'm going to be late from work at this rate. Can we deal with the homework tomorrow, maybe in the evening?"

            iv "Sorry, I can't make it in the evening."

            j "Me neither. How about the day after tomorrow?"

            iv "I've got things to do that day. Tomorrow afternoon would be fine by me."

            j "That's too bad. I've got tomorrow completely full already. What about you, [first_name]?"

            y "I've got both tomorrow and the day after tomorrow free."

            menu:

                j "Well, I guess it's up to you to choose who you want to do homework with."

                "[iv]" if not ivy_abandon:
                
                    call all_approve

                    y "I'll study with you, [iv]. If it's fine with you."

                    iv "Sure, whatever."

                    j "Then it's settled. We'll see each other on the next lesson then."

                    $ ivy_approve += 1
                    $ study = "i"

                "[j]" if not jasmine_abandon:
                    call all_approve

                    y "I'll study with you, [j], if you'll have me."

                    j "Of course! See you on the day after tomorrow, in the evening then?"

                    y "See you then."

                    j "Excellent. The rest of us will see each other on the next lesson then."

                    python:
                        jasmine_approve += 1
                        study = "j"

                "[r]" if not roger_abandon:
                    call all_approve

                    y "I'll study with you, [r], if you'd like."

                    r "Me? Okay, sure. See you tomorrow evening?"

                    y "See you then."

                    j "Excellent. The rest of us will see each other on the next lesson then."

                    python:
                        roger_approve += 1
                        study = "r"

                "I'll study by myself.":
                    call all_approve

                    j "Alright. Then we'll see each other at the next lesson."
                    $ study = "y"

                "I'll skip homework.":
                    jump all_disapprove

                    show jasmine casual up frown
                    show roger casual frown

                    if ivy_approve <= abandon_level and not ivy_abandon:
                        jump ivy_abandons
                        call all_disapprove

                    j "Seriously? Skip homework?"

                    y "Today's stuff was easy. I'll be fine."

                    j "Well-"

                    iv "It's your funeral."

                    j "Eh... I mean, I don't recommend skipping homework even if you feel you learned it all in one go, but you do you I guess."

                    $ study = "skip"
            
            r "Well, I gotta go now. See you all on the next lesson."

            "Roger leaves with an unusual hurry in his step. Ivy leaves as well."

            j "Well, looks like we should go on our separate ways too."

            y "Yeah..."

            if jasmine_abandon:

                j "Actually, before you go, there's something I should say."

                jump jasmine_abandons
            
            "You and [j] go on your separate ways."

            jump home


                



label home:

    play music "audio/Friday Afternoon Loop.ogg" loop

    if lesson == 1:

        scene bedroom_evening

        "Once you're done with your other homework, you spend some of your evening flipping through the course material. It's getting clearer and clearer that you have stepped way beyond your comfort zone."

        "That's probably a good thing, though. Your comfort zone has been too small for making other friends than Tamera, after all, so expanding is likely to help anyway."

        "Perhaps once you're done with this course, you could take some more German courses at school to try and get more friends there. The less you rely on Tamera to keep you company, the better."

        "..."

        "It's too early to decide that, though. One lesson and course at a time."

        jump school
    
    if lesson == 2:

        scene bedroom_evening

        "Since you agreed to do your homework for the German course tomorrow, you leave the materials be for the evening. At least hopefully you would get to know your fellow students a bit better then."

        jump school

    if lesson == 3:

        scene bedroom_evening
        if study == "y":
            "You do all the homework, including your German homework, alone in the evening. It's lonely work and you wonder if you should have studied with [iv] so that she would not have had to do the same work alone."

            "Honestly, studying alone was lame after the group homework session at the cafe. You should probably do your homework with the others when you can."
        
        elif study == "skip":
            "Once you were done with your other homework, you glanced at your German homework. The memory of the others' looks when you said that you'd skip doing it stung and you did consider doing the homework after all for a moment."
            
            "However, you were still confident you had learned the lesson's contents, so you left the homework undone."

        else:
            "Once you were done with your other homework, you glanced at your German homework. Since you had plans to do it tomorrow, you left it be."

        jump school

    if lesson == 4:

        scene bedroom_evening
        if study == "y":
            "You do all the homework, including your German homework, alone in the evening. It's lonely work and you wonder if you should have studied with someone else to give your studying a bit of a boost, to motivation if nowhere else."

            "Honestly, studying alone was lame after the group homework session at the cafe. You should probably do your homework with the others when you can."
        
        elif study == "skip":
            "Once you were done with your other homework, you glanced at your German homework. The memory of the others' looks when you said that you'd skip doing it stung and you did consider doing the homework after all for a moment."
            
            "However, you were still confident you had learned the lesson's contents, so you left the homework undone."

        else:
            "Once you were done with your other homework, you glanced at your German homework. Since you had plans to do it tomorrow, you left it be."

        jump school


label school:

    play music "audio/Monday Morning Loop.ogg" loop if_changed

    scene school_hallway_day

    if lesson == 1:

        "A couple of days later, as you hang out with Tamera for once during a break at school, you spot someone familiar. She appears to be alone, so since Tamera is - once again - occupied with her phone, you go to her."

        show ivy side casual frown

        y "Hi."

        ivm "..."

        y "You're on that German Basics course, right? [ivm], was it?"

        ivm "...What's it to you?"

        y "Well, I figured I could say hi since we're kinda acquainted."

        ivm "Well hi. Now leave me be."

        y "...Uh..."

        hide ivy

        "[iv] walks away, although not without giving you a weighty glare. You hear [t] howl in laughter behind you."

        t "Smooth, my friend, very smooth. Very charming pickup tactics."

        y "Shuddup. I was just trying to say hi."

        t "Yeah, right. Who's she anyway? You know 'er?"

        y "She's in my German course."

        t "What German course?"

        y "That German basics course I told you about, the one I started a couple of days ago."

        t "Oooh... Riiight. Yeah, that. Yeah, I toootally remember now."

        "You remind yourself that you {i}really{/i} need some new friends."

        "The bell rings. The show must go on."

        jump classroom

    if lesson == 2:

        "At school on the following day, you spot [ivm] again. This time, your eyes meet and she is quick to pointedly look away."

        "You hear Tamera snicker and figure it's for the best not to approach. One embarrassing incident per month was more than enough, after all."

        "Besides, you were going to see her in the evening at the cafe anyway."

        "The bell rings. You should head back to your classes."

        jump cafe

    if lesson == 3:

        "You spot [iv] at school while Tamera is... somewhere."

        if ivy_abandon:

            "She also spots you and glares at you. You figure that it's for the best not to approach her."
        
        else:

            "Since you've been getting closer to her (and Tamera isn't there to see and laugh if you get blown off again), you approach her."

            show ivy side casual frown

            iv "What?"

            y "Hallo. Wie geht's Ihnen?"

            "Ivy snorts."

            iv "You know we weren't taught how to respond to that question."

            y "..."

            y "...Oh. {i}Oh.{/i} Good point. Sorry."

            iv "No problem. At least you made the effort."

            iv "What brings you to me anyway?"

            y "I figured I could see if you're in the mood to talk."

            iv "Well... I really am not. But since you made the effort to speak German, I guess I don't mind your company for this break."

            if ivy_approve >= ivy_approve_friend_low:

                iv "..."

                iv "Actually... I think we could talk for a bit."

                y "Really?"

                iv "Yes."

                jump ivy_friended
        
        if study == "i" or study == "jr":
            
            jump cafe
        
        else:
            jump classroom

    if lesson == 4:

        "Tamera is elsewhere once again. Only now, you are starting to realize just how absent she has been in your life for a good while."
        
        "While looking around in boredom, you spot [iv]."

        if ivy_abandon:

            "She also spots you and glares at you. You figure that it's for the best not to approach her."
        
        if ivy_friend:

            "Since you're now friends with [iv], you walk up to her."

            y "Hi."

            show ivy side casual frown

            iv "Hi. Alone again?"

            y "So it seems. Besides, I just spotted you. I would've come to you if I'd seen you earlier."

            iv "I see. Well, at least you're here now. Do you want to talk about something?"

            y "I don't know. I didn't really have a plan for any of this."

            show ivy side casual smile

            iv "Fair enough. How about we just hang out?"

            y "Sounds good to me."

            "You spend the rest of the breaks together. You don't talk much, but having some good company is more than enough for you. You have a feeling that [iv] does not want any more than that anyway."

            "Only after you have said goodbye to [iv] upon leaving school you realize that you only saw Tamera at lessons today."
        
        else:

            "Since you've been getting closer to her (and Tamera isn't there to see and laugh if you get blown off again), you approach her."

            show ivy side casual frown

            iv "What?"

            y "Hallo. Wie geht's Ihnen?"

            "Ivy snorts."

            iv "You know we weren't taught how to respond to that question."

            y "..."

            y "...Oh. {i}Oh.{/i} Good point. Sorry."

            iv "No problem. At least you made the effort."

            iv "What brings you to me anyway?"

            y "I figured I could see if you're in the mood to talk."

            iv "Well... I really am not. But since you made the effort to speak German, I guess I don't mind your company for this break."

            if ivy_approve >= ivy_approve_friend_low:

                iv "..."

                iv "Actually... I think we could talk for a bit."

                y "Really?"

                iv "Yes."

                jump ivy_friended
        
        if study == "i" or study == "j" or study == "r":
            
            jump cafe
        
        else:
            jump classroom


            

label cafe:

    play music "audio/Calm Loop.ogg" loop if_changed

    scene cafeteria_day

    if lesson == 2:

        "At 18.30, you and your fellow German students gather around a table in the corner, books and drinks ready."

        show roger casual smile at center

        show jasmine casual up smile at right

        js "So, simple greetings and numbers 0-10. Shall we get started?"

        show ivy side casual frown at left

        ivm "Let's get this over with."

        js "You really aren't keen on this, are you?"

        ivm "Of course not. I'm missing practice because of the lessons."

        js "You do sport?"

        ivm "Judo."

        js "Oh, that's cool! I tried Aikido some years ago with [r] but it wasn't really my thing."

        ivm "Were we supposed to do our homework or chat?"

        js "Haha, right, sorry, I got a bit carried away. Anyhoo, first we have some greetings."

        ivm "\"Good afternoon\" is \"Guten Tag\"."

        show roger casual frown at center
        
        menu:
            rg "\Good evening\" was..... \"Guten...\" Um..."

            "Abend.":
                show roger casual smile

                rg "Right. \"Guten Abend.\""
                
                call all_approve
            
            "Abent.":

                js "\"Abend\", not \"Abent\". You almost got it, though."
            
            "Afternt.":

                call all_disapprove

                show jasmine casual up frown

                "[ivm] glares at you."

                ivm "Are you even trying?! It's \"Abend\". Guten Abend."
                
                y "Oh, right. My bad."

                "{i}Whoops!{/i}"

        
        "As you keep working on the exercise, you catch a glance at [ivm]'s notes. Despite her clear reluctance to be at the course, her notes are detailed and precise."

        "Unfortunately, [ivm] notices you watching."

        ivm "What?"

        y "Sorry, I got lost in thought."

        ivm "Well get lost in thought without staring at me."

        rg "Shall we move on to the other exercise?"

        ivm "Yeah, let's."

        js "Looks like very basic maths."

        rg "Yeah, we need to solve the calculations and write the answers in German."

        js "{i}Cool...{/i} The things I minored in maths for..."

        show roger casual smile

        "Roger snorts."

        rg "Didn't you always complain about the simple arithmetic mistakes when you worked on your math courses?"

        show jasmine casual up smile

        js "They were {i}the worst{/i}!"

        ivm "Can we {i}please{/i} stay on topic?"

        js "Right, sorry."

        python:
            wrong = numbers_wrong[6]
            correct = numbers_right[6]

        menu:

            js "Anyhoo, the first one's 2+4. Which is 6."

            "[correct]":
                js "Yeah, it's [correct]."
                call all_approve
            "[wrong]":
                js "Almost. It's actually [correct]."
            "zere":
                call all_disapprove
                show jasmine casual up frown
                show roger casual frown

                js "Yeah, no. It's [correct]."
            
        if ivy_approve <= abandon_level:

            jump ivy_abandons
            call all_disapprove

            rg "Um... How about we move on? The next one's 13-9. That's 4."

            ivm "It's vier."

            "You finish the rest of the exercises in a tense air. [ivm] leaves as soon as she is ready, only barely agreeing on the four of you being on first-name basis."

            "[r] leaves soon afterwards, leaving you and [j] to start walking home once you are done with your exercises."
        
        else:

            ivm "Next one's 13-9. It's 4."

            js "That's vier."
            
            "You finish the rest of the exercises in a casual air. [ivm] leaves as soon as she is ready, although she pauses just to agree on the four of you being on first-name basis."

            "[r] leaves some time later, leaving you and [j] to start walking home once you are done with your exercises."

        jump walk_home

        if lesson == 3:
            if study == "i":
                
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
                            jump ivy_abandons

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

                        iv "Huh. You actually seem to be taking this stuff seriously."
                
                iv "Moving on..."

                "You finish the homework in record time thanks to [iv]."

                iv "Well, we're done now. I must say, I'm impressed with you."

                y "Thanks."

                if ivy_approve >= ivy_approve_friend_low and not ivy_friend:

                    iv "..."

                    jump ivy_friended
                
                iv "We should call it a day now. See you at school. Or the next lesson."

                "With that, you both leave the cafe. You do not run into each other at school on the following days, instead only meeting when the next lesson starts."
            
            elif study == "jr":
                
                "You meet [j] and [r] at the cafe at 16.00."

                show jasmine casual smile at left
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

                    jump roger_friended

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

                    jump roger_abandons

                    "[r] leaves. You stay behind, figuring that you probably should let him and [j] head out first."

                    "You are definitely messing things up. You should probably pay more attention at the next lesson before even [j] decides that you're not good company."

                    jump classroom
                
                else:

                    r "Yeah, I'm ready to go."

                    j "Great. Let's go then."

                    jump walk_home
    if lesson == 4:

        if study == "i":

            "You meet [iv] at the cafe in the afternoon, as agreed yesterday."

            if ivy_friended:
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
                        jump ivy_abandons

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

                jump ivy_romanced

            elif ivy_approve >= ivy_approve_friend_low and not ivy_friend:

                iv "Before we finish for the day, there's something I'd like to talk about. Do you have some time?"

                y "Sure. I don't have any other plans than this meeting for today."

                iv "Good."

                jump ivy_friended

            iv "Alright. Time for me to head out. See you on the next lesson. And... thank you for this meeting."

            y "No, thank you. See you on the next lesson."

            "You go on your separate ways."
        
        if study == "r":

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
                        jump roger_abandons

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

                jump roger_romanced

            elif roger_approve >= roger_approve_friend_low and not roger_friend:

                show roger casual frown

                r "Um... are you in a hurry to go back home?"

                y "No. I've still got time before I need to leave."

                r "Ah, good... I'd like to hang out for a bit... I could use some company since [n] is at work."

                y "[n]?"

                r "Oh, right, you don't know. That's [j]'s nickname, although I don't think anyone except I use it."

                y "Oh, okay."

                y "Well, I do have time to hang out if you want to hang out with me."

                show roger casual smile

                r "I'm glad to hear that. I... I'd like to talk with you a bit more, after all..."

                jump roger_friended

            r "I guess we should get going. Thanks for today."

            y "No, thank you. See you on the next lesson."

            "You go on your separate ways."

            jump classroom

        if study == "j":

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
                        jump jasmine_abandons

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

            if jasmine_friended and jasmine_approve >= jasmine_approve_romance_low:

                j "I know it's getting a bit late, but would you mind sticking around for a bit?"

                y "I don't mind. Is there something on your mind?"

                j "Yes, there is."

                jump jasmine_romanced

            elif jasmine_approve >= jasmine_approve_friend_low and not jasmine_friend:

                j "I know it's getting a bit late, but would you mind staying for a bit?"

                y "I don't mind. Do you want to talk about something?"

                j "I do."

                jump jasmine_friended

            j "Again, thanks for coming today."

            y "No, thank you. Shall we walk home together?"

            j "Sounds good to me."

            "You head out into the evening."

            jump walk_home


label walk_home:

    play music "audio/Calm Loop.ogg" loop if_changed

    if lesson == 2:

        scene street_summer_evening

        show jasmine casual up smile

        js "I didn't expect us to live in the same neighborhood. A small world, huh?"

        y "Yeah, it sure is."

        "Now that you're not focusing on coursework, you notice a distinct yellow-white-purple-black pin on [j]'s bag."

        y "Is that pin on your bag the non-binary flag?"

        js "Yeah, it is. It's actually the first LGBT thing I ever got as a gift. [r] gave it to as a gift after I came out to him as an enby."

        js "Heh, he was the first one I ever even came out to. We've been besties since we were kids, so it was only natural that he was the first one to officially know."

        y "You think he suspected it before?"

        js "Well, considering that he was the one who suggested I look into the enby stuff in the first place, you bet he suspected something. And he suspected right."

        y "That's really cool."

        js "Yeah, it is. [r]'s really cool when he warms up to you, y'know. It takes time, but he's worth the patience he takes."

        y "I'll keep that in mind."

        js "You'd better."

        if jasmine_approve >= jasmine_approve_friend_low:
            call jasmine_friended

        js "Welp, this is where we have to go separate paths. See you on the next lesson, okay?"

        y "See you then."

        jump classroom

    if lesson == 3:

        scene street_summer_day

        show jasmine casual up smile

        y "Thanks for walking with me."

        j "No problem! I'm happy to hang out!"

        j "Have you liked the German course so far?"

        y "It's been fine. A bit too early to say much just yet. I mean, we've only had three lessons so far."

        j "True, true."

        if jasmine_approve >= jasmine_approve_friend_low and not jasmine_friend:

            jump jasmine_friended
        
        j "Looks like we need to go our separate ways now. See you at the next lesson, okay?"

        y "See you there."

        "You head home while [j] heads to work. You're already looking forward to the next lesson."

        jump classroom

    if lesson == 4:

        scene street_summer_evening

        show jasmine casual up smile

        "You walk with [j], talking about this and that."

        j "Oh, we're already here. Walks home sure are faster when you have someone to talk with."

        y "Yup!"

        j "Well, I guess we'll see each other on the next lesson then. See you then."

        y "See you!"

        "You and [j] go on your separate ways. You are already looking forward to your next lesson a lot."

        jump classroom

