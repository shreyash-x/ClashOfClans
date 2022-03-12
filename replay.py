import time
import os
from colorama import init
from colorama import Fore, Back, Style
from os.path import isfile, join
os.system('clear')

init(autoreset=True)


path = './replays'
onlyfiles = [f for f in os.listdir(path) if isfile(join(path, f))]

i=1

for file in onlyfiles:
    print(str(i)+ '.' + ' Replay-' + str(i) + ': ' + file.split('_')[1] +' '+ file.split('_')[2] )
    i+=1

print('\n')
ch = input('Enter the replay you want to play: ')

filename = path + '/' +onlyfiles[int(ch) - 1]

file = open(filename, 'r')

data = file.read()
file.close()

slides = data.split('=====')

for slide in slides:
    os.system('clear')
    print(slide)
    # add delay of 0.3 seconds
    time.sleep(0.3)