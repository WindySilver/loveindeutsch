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

    $renpy.call_screen("show_note", heading="Greetings", notesText="Guten Abend = Good evening\nGuten Tag = Good day\nHallo/Grüezi/Grüß Gott = Hello\nAuf Wiedersehen = Goodbye")

    return

label note_0_10:

    $renpy.call_screen("show_note", heading="Numbers 0-10", notesText="0 = null\n1 = eins\n2 = zwei\n3 = drei\n4 = vier\n5 = fünf\n6 = sechs\n7 = sieben\n8 = acht\n9 = neun\n10 = zehn")

    return