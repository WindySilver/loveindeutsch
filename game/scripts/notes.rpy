screen notes():
    modal True

    python:
        noteText = ""
        noteIndex = 0
        for i in notes:
            if i:
                if noteIndex == 1:
                    noteText = noteText + "{a=showmenu:note_greetings}Greetings{/a}\n"
                    noteText = noteText + "{a=showmenu:note_0_10}Numbers 0-10{/a}\n"
                if noteIndex == 2:
                    noteText = noteText + "{a=showmenu:present}Presenting oneself{/a}\n"
                if noteIndex == 3:
                    noteText = noteText + "{a=showmenu:greetings_goodbyes}More greetings + goodbyes{/a}\n"
                else:
                    noteText = noteText + ""
            noteIndex += 1

    frame:
        xpadding 200
        ypadding 200
        xalign 0.5
        yalign 0.5

        viewport:
            vbox:
                text "{size=35}Notes{/size}"
                text noteText
                textbutton "OK" action Return()

screen show_note(heading, notesText):
    modal True

    frame:
        xpadding 200
        ypadding 200
        xalign 0.5
        yalign 0.5

        viewport:
            vbox:
                text "{size=35}[heading]{/size}"
                text [notesText]
                textbutton "OK" action ShowMenu("notes")

label note_greetings:

    $ renpy.call_screen("show_note", heading="Greetings", notesText="Guten Abend = Good evening\nGuten Tag = Good day\nHallo/Grüezi/Grüß Gott = Hello\nAuf Wiedersehen = Goodbye")

    return

label note_0_10:

    $ renpy.call_screen("show_note", heading="Numbers 0-10", notesText="0 = null\n1 = eins\n2 = zwei\n3 = drei\n4 = vier\n5 = fünf\n6 = sechs\n7 = sieben\n8 = acht\n9 = neun\n10 = zehn")

    return

label present:

    $ renpy.call_screen("show_note", heading="Presenting oneself", notesText="be named = heißen\nMy name is Patrick = Ich heiße Patrick\nI am Patrick = Ich bin Patrick\nShe is Lisa = Sie ist Lisa\nNice to meet you = Freut mich\nHow are you = wie geht's dir (with friends) or wie geht's Ihnen (more polite)")

label greetings_goodbyes:

    $ renpy.call_screen("show_note", heading="Greetings and goodbyes", notesText="Good morning = Guten Morgen\nGood night = Gute Nacht\nAuf Wiedersehen = Goodbye\nTschüss = bye")