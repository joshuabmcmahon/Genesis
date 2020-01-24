from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import messagebox
from synthesizer import Player, Synthesizer, Waveform

NOTES = [
 	 	 	 
    ("C3","130.813"),
    ("C#/Db3","138.591"), 
    ("D3","146.832"),
    ("D#/Eb3","155.563"),
    ("E3","164.814"),
    ("F3","174.614"),
    ("F#/Gb3","184.997"),	 
    ("G3","195.998"),
    ("G#/ Ab3","207.652"),	 
    ("A3","220"),
    ("A#/Bb3","233.082"), 
    ("B3","246.942"),	 
 	 	 	 	 
    ("C4","261.626"),
    ("C#/Db4","277.183"),
    ("D4","293.665"),
    ("D#/Eb4","311.127"), 
    ("E4","329.628"),
    ("F4","349.228"),
    ("F#/Gb4","369.994"),	 
    ("G4","391.995"),
    ("G#/Ab4","415.305"),	 
    ("A4","440"),
    ("A#/Bb4","466.164"),	 
    ("B4","493.883"), 
]


root=Tk()
root.title("The 6th Dimension's CHORDPLAYER")
root.iconbitmap("/Users/SIX/Pictures/VS \PYTHON/ICONS/sixsign.ico")

chord_to_play = []
notes = DoubleVar()
for name, freq in NOTES:(
    Checkbutton(root, text=name, variable=freq).grid()
    )

def play():
    player = Player()
    player.open_stream()
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    player.play_wave(synthesizer.generate_chord(float(freq), 1.0))



PLAY = Button(root, text="PLAY", command=play).grid()

root.mainloop()