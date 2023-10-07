from audiolazy import str2midi
from midiutil import MIDIFile
import pandas as pd
import matplotlib.pylab as plt
import pickle

colors_col = pickle.load(open("colors_col_exoplanet", "rb"))

def map_value(value, min_value, max_value, min_result, max_result):

    result = min_result + (value - min_value)/(max_value - min_value)*(max_result - min_result)
    return result
    
df = pd.DataFrame(colors_col, columns =["Red", "Green", "Blue", "Brightness"])
n_colors = len(df)
blue = df["Blue"].values
brightness = df["Brightness"].values
red = df["Red"].values

blue = max(blue) - blue

duration_beats = 60

t_data = map_value(blue, 0, max(blue), 0, duration_beats)


blue_per_beat = max(blue)/duration_beats
print("Blue per beat:", blue_per_beat)

bpm = 60  
duration_sec = duration_beats*60/bpm 
print("Duration:", duration_sec, "seconds")

y_data_brightness = map_value(brightness, min(brightness), max(brightness), 0, 1)
y_data_red = map_value(red, min(red), max(red), 0, 1)

y_scale = 0.5 

y_data_brightness = y_data_brightness**y_scale
y_data_red = y_data_red**y_scale

plt.figure("Blue data to time data")
plt.scatter(t_data, y_data_red)
plt.xlabel('Time [beats]')
plt.ylabel('Red [normalized]')
plt.show()

note_names = ["C2","D2","E2","G2","A2",
             "C3","D3","E3","G3","A3",
             "C4","D4","E4","G4","A4",
             "C5","D5","E5","G5","A5"]

note_midis = [str2midi(n) for n in note_names]

n_notes = len(note_midis)
print("Resolution:",n_notes, "notes")

midi_data = []
for i in range(n_colors):
    note_index = round(map_value(y_data_red[i], 0, 1, n_notes-1, 0))
                                                        
    midi_data.append(note_midis[note_index])

plt.figure("Red data to music data")
plt.scatter(t_data, midi_data)
plt.xlabel('Time')
plt.ylabel('Midi')
plt.show()

vel_min, vel_max = 35,127   

vel_data = []
for i in range(n_colors):
    note_velocity = round(map_value(y_data_brightness[i], 0, 1, vel_min, vel_max)) 
    vel_data.append(note_velocity)

plt.figure("Brightness data to vel data")    
plt.scatter(t_data, vel_data)
plt.xlabel("Time")
plt.ylabel("Vel")
plt.show()
plt.figure("Music")    
plt.scatter(t_data, midi_data, s=vel_data)
plt.xlabel("Time")
plt.ylabel("Midi")
plt.show()

my_midi_file = MIDIFile(1) 
my_midi_file.addTempo(track=0, time=0, tempo=bpm) 

for i in range(n_colors):
    my_midi_file.addNote(track=0, channel=0, pitch=midi_data[i], time=t_data[i], duration=2, volume=vel_data[i])

#with open('Nasa Space App Challenge' + '1 minute seconds.mid', "wb") as f:
#    my_midi_file.writeFile(f) 
