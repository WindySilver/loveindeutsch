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
                    study = "jr"

            "I'll study by myself.":
                call all_approve

                j "Alright. Then we'll see each other at the next lesson. Bye now!"
                $ study = "y"

            "I'll skip homework.":
                call all_disapprove

                show jasmine casual up frown
                show roger casual frown

                if ivy_approve <= abandon_level and not ivy_abandon:
                    call ivy_abandons
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
            call roger_abandons
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

            call roger_friended

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

                show roger casual smile

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

                call all_disapprove

                show jasmine casual up frown

                show roger casual frown

                if ivy_approve <= abandon_level and not ivy_abandon:

                    call ivy_abandons

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

            call jasmine_abandons

        

        "You and [j] go on your separate ways."

        jump home
    return


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

        python:
            if study == "y":
                renpy.call("alone")
            elif study == "skip":
                renpy.call("skip_studying")
            else:
                renpy.call("plans")

        jump school

    if lesson == 4:

        scene bedroom_evening

        python:
            if study == "y":
                renpy.call("alone")
            elif study == "skip":
                renpy.call("skip_studying")
            else:
                renpy.call("plans")

        jump school
    return


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

                call ivy_friended
        
        python:
            if study == "i" or study == "jr":
                renpy.jump("cafe")
        
            else:
                renpy.jump("classroom")

    if lesson == 4:

        "Tamera is elsewhere once again. Only now, you are starting to realize just how absent she has been in your life for a good while."
        
        "While looking around in boredom, you spot [iv]."

        if ivy_abandon:

            "She also spots you and glares at you. You figure that it's for the best not to approach her."
        
        elif ivy_friend:

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

                call ivy_friended
        
        python:

            if study == "i" or study == "j" or study == "r":
                renpy.jump("cafe")

            else:
                renpy.jump("classroom")
    return


            

label cafe:

    play music "audio/Calm Loop.ogg" loop if_changed

    scene cafeteria_day

    if lesson == 2:

        "At 18.30, you and your fellow German students gather around a table in the corner, books and drinks ready."

        show roger casual smile at center

        show jasmine casual up smile at right

        show ivy side casual frown at left

        js "So, simple greetings and numbers 0-10. Shall we get started?"

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
            wrong = numbers_wrong[5]
            correct = numbers_right[5]

        menu:

            js "Anyhoo, the first one's 2+3. Which is 5."

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

            call ivy_abandons
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
        python:
            if study == "i":
                renpy.call("ivy_studying")
            elif study == "jr":
                renpy.call("jasmine_roger_studying")
            else:
                renpy.call("error")
                
    if lesson == 4:
        python:
            if study == "i":
                renpy.call("ivy_studying")
            
            elif study == "j":
                renpy.call("jasmine_studying")
            
            elif study == "r":
                renpy.call("roger_studying")
            else:
                renpy.call("error")
    return
                


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

            call jasmine_friended
        
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
    return


label error:

    "Dev" "Something has gone wrong. Please let the developer know."