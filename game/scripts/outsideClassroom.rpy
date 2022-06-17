label outside:
    
    if lesson == 1:
        
        scene school_hallway_day
        
        "Your head is filled with information on what the course consists of and the tests and homework you will need to do to pass."
        
        "This had better be worth it."
        
        "You see [rg] and [js] talking with one another. You take a few steps towards them, hoping you could talk to them, but their conversation seems to turn into an argument."
        
        "It's probably for the best not to get involved. You turn back and head home. Perhaps you'll have better luck with the next lesson when everything is supposed to truly kick off..."
        
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

label school:

    if lesson == 1:

        scene school_hallway_day

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