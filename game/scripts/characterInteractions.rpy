label ivy_abandons:
    $ ivy_abandon = True
            
    ivm "You're not trying at all, are you? Why did you even enroll on the course?"

    y "I, uh, I... Well, I wanted to make new friends."

    ivm "Well, you definitely aren't working for it. I'm not here to chat or make friends, I'm here because I have to."

    ivm "The fact that you're here voluntarily and are messing around pisses me off."

    y "Sorry..."

label roger_abandons:
    $ roger_abandon = True
            
    rg "Look, this isn't working out."

    y "Huh?"

    rg "[j] dragged me to the German course, so I'd better at least put enough effort to get through it. You clearly aren't."
    
    rg "I've been dragged down by bad influences too many times in my life already to keep any around. I'm sorry, I really am, but I have to cut you out."

    rg "You seem really nice and in other circumstances we could've been good friends, but I can't afford to lose my grip on this course."

    rg "I should get going. Goodbye, [full_name]."

label jasmine_abandons:
    $ jasmine_abandon = True
            
    "[js] sighs."

    js "Look, I've given you the benefit of the doubt. [r] sometimes loses his focus on stuff and someone needs to knock some sense into him. I figured you might be the same."

    js "But you aren't trying at all, are you? You aren't trying to learn anything. You're just trying to get friends and have fun."

    js "I'm not here for that. I'm on this course to learn. If you can't put in even the slightest effort to do that, then this won't work out."

    y "Sorry. I... I guess I got carried away or something."

    js "I suppose. In any case, I'm done. See you on the remaining lessons... if you even bother to show anymore."