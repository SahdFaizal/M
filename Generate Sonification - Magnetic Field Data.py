from audiolazy import str2midi
from midiutil import MIDIFile
import pandas as pd
import matplotlib.pylab as plt
#import pickle

df = pd.read_csv('themis_carisma_overlap_data.csv')
df = df.drop(columns=['Index'])
df = df.drop(columns=['Geog Lat  (deg)'])
df = df.drop(columns=['Geog Long (deg)'])
df = df.drop(columns=['Name'])
df = df.drop(columns=['Geom Lat (deg)'])
df = df.drop(columns=['Geom Long (deg)'])

def map_value(value, min_value, max_value, min_result, max_result):

    result = min_result + (value - min_value)/(max_value - min_value)*(max_result - min_result)
    return result

    
df = pd.DataFrame(df, columns =["2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018"])
n_2006 = df["2006"].values
n_2007 = df["2007"].values
n_2008 = df["2008"].values
n_2009 = df["2009"].values
n_2010 = df["2010"].values
n_2011 = df["2011"].values
n_2012 = df["2012"].values
n_2013 = df["2013"].values
n_2014 = df["2014"].values
n_2015 = df["2015"].values
n_2016 = df["2016"].values
n_2017 = df["2017"].values
n_2018 = df["2018"].values

allValues = []

for i in range(len(n_2006)):
        allValues.append(n_2006[i])
        
for i in range(len(n_2007)):
        allValues.append(n_2007[i])
        
for i in range(len(n_2008)):
        allValues.append(n_2008[i])
        
for i in range(len(n_2009)):
        allValues.append(n_2009[i])
        
for i in range(len(n_2010)):
        allValues.append(n_2010[i])
        
for i in range(len(n_2011)):
        allValues.append(n_2011[i])
    
for i in range(len(n_2012)):
        allValues.append(n_2012[i])

for i in range(len(n_2013)):
        allValues.append(n_2013[i])

for i in range(len(n_2014)):
        allValues.append(n_2014[i])
        
for i in range(len(n_2015)):
        allValues.append(n_2015[i])

for i in range(len(n_2016)):
        allValues.append(n_2016[i])
        
for i in range(len(n_2017)):
        allValues.append(n_2017[i])

for i in range(len(n_2018)):
        allValues.append(n_2018[i])
        
n_values = len(allValues)

Time = max(allValues) - allValues

duration_beats = 60

t_data = map_value(Time, 0, max(Time), 0, duration_beats)

Time_per_beat = max(Time)/duration_beats
print("Time per beat:", Time_per_beat)

bpm = 60  
duration_sec = duration_beats*60/bpm 
print("Duration:", duration_sec, "seconds")

y_data = map_value(allValues, min(allValues), max(allValues), 0, 1)

y_scale = 0.5 

y_data = y_data ** y_scale

plt.figure("T_data [normalized]")
plt.scatter(t_data, y_data)
plt.xlabel('Time[beats]')
plt.ylabel('Y_data [normalized]')
plt.show()

note_names = ["C2","D2","E2","G2","A2",
             "C3","D3","E3","G3","A3",
             "C4","D4","E4","G4","A4",
             "C5","D5","E5","G5","A5"]

note_midis = [str2midi(n) for n in note_names]

n_notes = len(note_midis)
print("Resolution:",n_notes, "notes")

midi_data = []
for i in range(n_values):
    note_index = round(map_value(y_data[i], 0, 1, n_notes-1, 0))
                                                        
    midi_data.append(note_midis[note_index])

plt.figure("Y_data to music data")
plt.scatter(t_data, midi_data)
plt.xlabel('Time')
plt.ylabel('Midi')
plt.show()

vel_min, vel_max = 35,127   

vel_data = []
for i in range(n_values):
    note_velocity = round(map_value(y_data[i], 0, 1, vel_min, vel_max)) 
    vel_data.append(note_velocity)

plt.figure("Y_data to vel data")    
plt.scatter(t_data, vel_data)
plt.xlabel("Time")
plt.ylabel("Vel")
plt.show()
plt.figure("Music")    
plt.scatter(t_data, midi_data, s=vel_data)
plt.xlabel("Time")
plt.ylabel("Midi")
plt.show()
#colors = []
#for i in range(len(allValues)):

#    colors.append((map_value(midi_data[i], max(midi_data), min(midi_data), 0, 255), map_value(vel_data[i], min(vel_data), max(vel_data), 0, 255), map_value(t_data[i], min(t_data), max(t_data), 0, 255)))
    
#pickle.dump(colors, open("colors_magnetic_field", "wb"))

my_midi_file = MIDIFile(1) 
my_midi_file.addTempo(track=0, time=0, tempo=bpm) 

for i in range(n_values):
    my_midi_file.addNote(track=0, channel=0, pitch=midi_data[i], time=t_data[i], duration=2, volume=vel_data[i])

#with open('Nasa Space App Challenge' + '1 minute seconds Magnetic Field.mid', "wb") as f:
#    my_midi_file.writeFile(f) 
