import wav
import mic
import silence
import transmitter


print('Welcome to radio-station!')
print('Available commands:')
print('play filename - play a wav file (no need to provide the extension)')
print('mic - stream real-time audio from the microphone')
print('stop - silence the radio, but keep running')
print('exit - quit this program')


while True:
    print('Enter command: ', end='')
    command = input()
    if command.find('play ') == 0:
        filename = command[len('play '):]
        transmitter.transmit(wav.stream(filename=filename))
    elif command == 'mic':
        transmitter.transmit(mic.stream())
    elif command == 'stop':
        transmitter.transmit(silence.stream())
    elif command == 'exit':
        exit() # transmitter automatically terminates subprocesses at exit
    else:
        print('Command not recognized!')
