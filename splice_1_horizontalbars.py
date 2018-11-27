import os
import shutil
import glob
import time
from pydub import AudioSegment
from pydub.utils import make_chunks

#FFMpeg filepath
AudioSegment.converter = r"C:\\path\\to\\ffmpeg.exe"

signal1 = AudioSegment.from_file("signal1.wav", "wav")
splice1_count = 0
signal2 = AudioSegment.from_file("signal2.wav", "wav")
splice2_count = 0
bigger = splice2_count

#pydub calculates in millisec
splice_length = 10000 

splices1 = make_chunks(signal1, splice_length)  
splices2 = make_chunks(signal2, splice_length)

os.mkdir("splices")
os.mkdir("splice_pairs")

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

#Recombinate individual splices using x1, y1, x2, y2, x3... switching pattern

#Use smaller file for length
if splice1_count < splice2_count:
    bigger = splice1_count
else:
    bigger = splice2_count

print splice1_count
print splice2_count
print bigger

#export audio pairs
for i in range(0, bigger):
    sound1 = AudioSegment.from_wav("splices/splices1_{0}.wav".format(i))
    sound2 = AudioSegment.from_wav("splices/splices2_{0}.wav".format(i))
    spliced_audio = sound1 + sound2
    spliced_audio_name = "spliced_audio_{0}.wav".format(i)
    print "exporting spliced audio pairs:", spliced_audio_name
    spliced_audio.export("splice_pairs/" + spliced_audio_name, format="wav")

#combine pairs into spliced_audio_final
#empty .wav file variable
spliced_audio_final = AudioSegment.empty()
count = 0

for splice in glob.glob('splice_pairs/*.wav'): 
    print "reconstituting segment", count 
    spliced_audio_final += AudioSegment.from_wav(splice)
    count += 1

print "exporting", "final spliced audio"
spliced_audio_final.export("spliced.wav", format="wav")

file_path = "c:/Users/dwt46/Documents/2018 4 Fall/Qualifying Project/recordings/splices/spliced.wav" 

if os.path.isfile(file_path):
    shutil.rmtree('splices')
    shutil.rmtree('splice_pairs')
















