from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import messagebox
from synthesizer import Player, Synthesizer, Waveform

###DATA

NOTES = [ 
    ("C4","261.6"),
    ("D4","293.7"),
    ("E4","329.6"),
    ("F4","349.2"),
    ("G4","392"),
    ("A4","440"),
    ("B4","493.9"),
    ]



##################MAIN PROGRAM#########################

root=Tk()
root.title("")
root.iconbitmap("/Users/SIX/Pictures/VS \PYTHON/ICONS/sixsign.ico")

notefreq=float

    
def play():
    player = Player()
    player.open_stream()
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    player.play_wave(synthesizer.generate_constant_wave(440.0, 1.0))


frame_notes = LabelFrame(root, text="NOTES", padx=50, pady=50)
frame_notes.pack(padx=10, pady=10)

Radiobutton(frame_notes, text="C4", variable=notefreq, value=261.6).pack()
Radiobutton(frame_notes, text="D4", variable=notefreq, value=293.7).pack()
Radiobutton(frame_notes, text="E4", variable=notefreq, value=329.6).pack()
Radiobutton(frame_notes, text="F4", variable=notefreq, value=349.2).pack()
Radiobutton(frame_notes, text="G4", variable=notefreq, value=392).pack()
Radiobutton(frame_notes, text="A4", variable=notefreq, value=440).pack()
Radiobutton(frame_notes, text="B4", variable=notefreq, value=493.9).pack()
btn = Button(root, text="Play Note", command=play).pack()



frame_chord = LabelFrame(root, text="CHORDS", padx=50, pady=50)
frame_chord.pack(padx=10, pady=10)

Radiobutton(frame_chord, text="Major", variable=notefreq, value=261.6).pack()
Radiobutton(frame_chord, text="Minor", variable=notefreq, value=293.7).pack()
Radiobutton(frame_chord, text="Diminished", variable=notefreq, value=329.6).pack()
Radiobutton(frame_chord, text="Major Seventh", variable=notefreq, value=349.2).pack()
Radiobutton(frame_chord, text="Minor Seventh", variable=notefreq, value=392).pack()



frame_scale = LabelFrame(root, text="SCALE", padx=50, pady=50, bg="yellow")
frame_scale.pack(padx=100, pady=100)



#btn = Button(root, text="Play Sound", command=play).pack()




root.mainloop()