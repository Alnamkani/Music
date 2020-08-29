import os 

names = open("names", 'r');
lines = names.readlines()
x = 1
for line in lines:
   os.system("ffmpeg -i " + "\"" + line.strip('\n') + "\" " + "song" + str(x) + '.mp3\n')
   x += 1
    
