from midiutil import MIDIFile
from random import randint

# Define the chords
chords = [[60, 64, 67], [62, 65, 69], [64, 67, 71], [65, 69, 72], [67, 71, 74]]

# Create a new MIDI file for the melody
melody_midi = MIDIFile(1)
melody_midi.addTempo(0, 0, 128)
melody_notes = [60, 62, 64, 65, 67]
for i in range(32):
    chord = chords[i % len(chords)]
    note = melody_notes[i % len(melody_notes)]
    while note not in chord:
        note += 1
    melody_midi.addNote(0, 0, note , i *5/4 ,5/4 ,100)
with open("melody.mid", "wb") as output_file:
    melody_midi.writeFile(output_file)

# Create a new MIDI file for the bass
bass_midi = MIDIFile(1)
bass_midi.addTempo(0, 0, 128)
bass_notes = [48, 50, 52, 53, 55]
for i in range(32):
    chord = chords[i % len(chords)]
    note = bass_notes[i % len(bass_notes)]
    while note not in chord:
        note += 12
    bass_midi.addNote(0 ,0 ,note ,i *5/4 ,5/4 ,100)
with open("bass.mid", "wb") as output_file:
    bass_midi.writeFile(output_file)

# Create a new MIDI file for the arpeggio
arpeggio_midi = MIDIFile(1)
arpeggio_midi.addTempo(0 ,0 ,128)
arpeggio_notes = [60 ,64 ,67]
for i in range(32):
    chord = chords[i % len(chords)]
    for j in range(3):
        note = chord[j]
        arpeggio_midi.addNote(0 ,0 ,note ,i *5/4 +j *(5/4 /3) ,(5/4 /3) ,randint(70 ,100))
with open("arpeggio.mid", "wb") as output_file:
    arpeggio_midi.writeFile(output_file)

# Create a new MIDI file for the percussion
percussion_midi = MIDIFile(1)
percussion_midi.addTempo(0 ,0 ,128)
percussion_notes = [35]
for i in range(32):
    percussion_midi.addNote(0 ,9 ,percussion_notes[0] ,i *5/4 ,(5/4 /2) ,randint(70 ,100))
with open("percussion.mid", "wb") as output_file:
    percussion_midi.writeFile(output_file)

# Create a new MIDI file for the string section
string_midi = MIDIFile(1)
string_midi.addTempo(0 ,0 ,128)
string_notes = [55 ,59 ,62]
for i in range(32):
    chord = chords[i % len(chords)]
    for j in range(3):
        note = chord[j]
        string_midi.addNote(0 ,3 ,note ,i *5/4 ,(5/4 /2) ,randint(70 ,100))
with open("string.mid", "wb") as output_file:
    string_midi.writeFile(output_file)