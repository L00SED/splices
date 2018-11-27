import os
import shutil
import glob
import time
import random
from pydub import AudioSegment
from pydub.utils import make_chunks


#FFMpeg filepath
AudioSegment.converter = r"C:\\path\\to\\ffmpeg.exe"

signal1 = AudioSegment.from_file("signal1.wav", "wav")
splice1_count = 0
signal2 = AudioSegment.from_file("signal2.wav", "wav")
splice2_count = 0
signal3 = AudioSegment.from_file("signal3.wav", "wav")
splice3_count = 0
signal4 = AudioSegment.from_file("signal4.wav", "wav")
splice4_count = 0
signal5 = AudioSegment.from_file("signal5.wav", "wav")
splice5_count = 0

bigger = splice1_count

#pydub calculates in millisec (this is the frame width)
splice_length1 = 73050
splice_length2 = 85000
splice_length3 = 30050
splice_length4 = 101350
splice_length5 = 91350

splices1 = make_chunks(signal1, splice_length1)  
splices2 = make_chunks(signal2, splice_length2)
splices3 = make_chunks(signal3, splice_length3)
splices4 = make_chunks(signal4, splice_length4)
splices5 = make_chunks(signal5, splice_length5)

os.mkdir("splices")
os.mkdir("splice_pentas")

#Export all of the individual chunks as wav files
for i, splice in enumerate(splices1):
    splice_name = "splices1_{0}.wav".format(i)
    print "exporting", splice_name
    splice.export("splices/" + splice_name, format="wav")
    splice1_count += 1
    print "splice1 count", splice1_count

for i, splice in enumerate(splices2):
    splice_name = "splices2_{0}.wav".format(i)
    print "exporting", splice_name
    splice.export("splices/" + splice_name, format="wav")
    splice2_count += 1
    print "splice2 count", splice2_count

for i, splice in enumerate(splices3):
    splice_name = "splices3_{0}.wav".format(i)
    print "exporting", splice_name
    splice.export("splices/" + splice_name, format="wav")
    splice3_count += 1
    print "splice3 count", splice3_count

for i, splice in enumerate(splices4):
    splice_name = "splices4_{0}.wav".format(i)
    print "exporting", splice_name
    splice.export("splices/" + splice_name, format="wav")
    splice4_count += 1
    print "splice4 count", splice4_count

for i, splice in enumerate(splices5):
    splice_name = "splices5_{0}.wav".format(i)
    print "exporting", splice_name
    splice.export("splices/" + splice_name, format="wav")
    splice5_count += 1
    print "splice5 count", splice5_count

#Recombinate individual splices using a1, b1, c1, d1, e1, a2, b2, c2, d2, e2, a3... switching pattern

#Use smaller file for length
bigger = min( splice1_count, splice2_count, splice3_count, splice4_count, splice5_count )


print splice1_count
print splice2_count
print splice3_count
print splice4_count
print splice5_count
print bigger

#export audio pentas
for i in range(0, bigger):
    sound1 = AudioSegment.from_wav("splices/splices1_{0}.wav".format(i))
    sound2 = AudioSegment.from_wav("splices/splices2_{0}.wav".format(i))
    sound3 = AudioSegment.from_wav("splices/splices3_{0}.wav".
format(i))
    sound4 = AudioSegment.from_wav("splices/splices4_{0}.wav".format(i))
    sound5 = AudioSegment.from_wav("splices/splices5_{0}.wav".format(i))

    spliced_audio = sound1 + sound2 + sound3 + sound4 + sound5
    spliced_audio_name = "spliced_audio_{0}.wav".format(i)
    print "exporting spliced audio pentas:", spliced_audio_name
    spliced_audio.export("splice_pentas/" + spliced_audio_name, format="wav")

#combine pairs into spliced_audio_final
#empty .wav file variable
spliced_audio_final = AudioSegment.empty()
count = 0

for splice in glob.glob('splice_pentas/*.wav'): 
    print "reconstituting segment", count 
    spliced_audio_final += AudioSegment.from_wav(splice)
    count += 1

print "exporting", "final spliced audio"
spliced_audio_final.export("spliced.wav", format="wav")

file_path = "c:/Users/dwt46/Documents/2018 4 Fall/Qualifying Project/recordings/splices/spliced.wav" 

if os.path.isfile(file_path):
    shutil.rmtree('splices')
    shutil.rmtree('splice_pentas')
















