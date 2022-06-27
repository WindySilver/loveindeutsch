label outside:
    
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


label home:

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

label school:

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

label cafe:

    scene cafeteria_day

    if lesson == 2:

        "At 18.30, you and your fellow German students gather around a table in the corner, books and drinks ready."

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
                
                jump all_approve
            
            "Abent.":

                js "\"Abend\", not \"Abent\". You almost got it, though."
            
            "Afternt.":

                jump all_disapprove

                show jasmine casual up frown

                "[ivm] glares at you."

                ivm "Are you even trying?! It's \"Abend\". Guten Abend."
                
                y "Oh, right. My bad."

                "{i}Whoops!{/i}"

        
        "As you keep working on the exercise, you catch a glance at [ivm]'s notes. Despite her clear reluctance to be at the course, her notes are detailed and precise."

        "Unfortunately, [ivm] notices you watching."

        ivm "What?"

        y "Sorry, I got lost in thought."

        ivm "Well get lost in thought so that you're not staring at me."

        # TODO the number exercise, setting first-name basis, going home on the same route as Jasmine




