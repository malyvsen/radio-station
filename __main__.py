import wav
import mic
import silence
import transmitter

import time


print('Welcome to radio-station!')
print('Available commands:')
print('play filename - play a wav file from audio/ (no need to provide extension)')
print('mic - stream real-time audio from the microphone')
print('stop - silence the radio, but keep running')
print('exit - quit this program')
print()


while True:
    command = input('Enter command: ')
    if command.find('play ') == 0:
        filename = command[len('play '):]
        transmitter.transmit(wav.stream(filename=filename))
    elif command == 'mic':
        transmitter.transmit(mic.stream())
    elif command == 'stop':
        transmitter.transmit(silence.stream())
    elif command == 'exit':
        exit() # processes are closed at exit
    else:
        print('Command not recognized!')
    time.sleep(.5) # give time for subprocesses to set up and display any warnings
