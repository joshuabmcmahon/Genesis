from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import messagebox
from synthesizer import Player, Synthesizer, Waveform

###DATA
'''
NOTES = [ 
    ("C4","261.6"),
    ("D4","293.7"),
    ("E4","329.6"),
    ("F4","349.2"),
    ("G4","392"),
    ("A4","440"),
    ("B4","493.9"),
    ]
'''


##################MAIN PROGRAM#########################

root=Tk()
root.title("The 6th Dimension's OSCILLISYNTH")
root.iconbitmap("/Users/SIX/Pictures/VS \PYTHON/ICONS/sixsign.ico")




notefreq=float
pwrval1 = IntVar()
pwrval2 = IntVar()
pwrval3 = IntVar()


frame_osc = LabelFrame(root, text="OSCILLATOR", padx=10, pady=10)
frame_osc.grid(row=0, column=0, padx=10, pady=10)

osc1 = Scale(frame_osc,  from_=200, to=400)
osc1.grid(row=1, column=0)
osc2 = Scale(frame_osc, from_=400, to = 600)
osc2.grid(row=1, column=1)
osc3 = Scale(frame_osc,from_= 600, to = 1000)
osc3.grid(row=1, column=2)

pwr1 = Checkbutton(frame_osc,text="OSC1",variable=pwrval1)
pwr1.grid(row=0,column=0)
pwr2 = Checkbutton(frame_osc,text="OSC2",variable=pwrval2)
pwr2.grid(row=0,column=1)
pwr3 = Checkbutton(frame_osc,text="OSC3",variable=pwrval3)
pwr3.grid(row=0,column=2)

frame_notes = LabelFrame(root, text="NOTES", padx=10, pady=10)
frame_notes.grid(row=1, column=0, padx=10, pady=10)

Radiobutton(frame_notes, text="C4", variable=notefreq, value=261.6).pack()
Radiobutton(frame_notes, text="D4", variable=notefreq, value=293.7).pack()
Radiobutton(frame_notes, text="E4", variable=notefreq, value=329.6).pack()
Radiobutton(frame_notes, text="F4", variable=notefreq, value=349.2).pack()
Radiobutton(frame_notes, text="G4", variable=notefreq, value=392).pack()
Radiobutton(frame_notes, text="A4", variable=notefreq, value=440).pack()
Radiobutton(frame_notes, text="B4", variable=notefreq, value=493.9).pack()
#btn = Button(root, text="Play Note", command=play).pack()



frame_chord = LabelFrame(root, text="CHORDS", padx=10, pady=10)
frame_chord.grid(row=1, column=1, padx=10, pady=10)

Radiobutton(frame_chord, text="Major", variable=notefreq, value=261.6).pack()
Radiobutton(frame_chord, text="Minor", variable=notefreq, value=293.7).pack()
Radiobutton(frame_chord, text="Diminished", variable=notefreq, value=329.6).pack()
Radiobutton(frame_chord, text="Major Seventh", variable=notefreq, value=349.2).pack()
Radiobutton(frame_chord, text="Minor Seventh", variable=notefreq, value=392).pack()



#frame_scale = LabelFrame(root, text="SCALE", padx=50, pady=50, bg="yellow")
#frame_scale.pack(padx=100, pady=100)



#btn = Button(root, text="Play Sound", command=play).pack()




root.mainloop()