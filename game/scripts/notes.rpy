screen notes:
    modal True

    python:
        noteText = ""
        noteIndex = 0
        for i in notes:
            noteIndex += 1
            if i:
                if noteIndex == 1:
                    noteText = noteText + "{a=showmenu:note_1}Greetings + 0-10{/a}\n"
                else:
                    noteText = noteText + ""

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
                textbutton "OK" action Return() 

label note_1:

    $renpy.call_screen("show_note", heading="Greetings + 0-10", notesText="Guten Abend = Good evening\nGuten Tag = Good day\nHallo = Hello\n\n0 = ?")


    