import wav
import mic
import transmitter


print('Welcome to radio-station!')
print('Available commands:')
print('play - play a wav file')
print('mic - stream real-time audio from the microphone')
print('exit - quit this program')


while True:
    print('Enter command: ')
    command = input()
    if command == 'play':
        print('Enter filename (without extension): ')
        transmitter.transmit(wav.stream(filename=input()))
    elif command == 'mic':
        transmitter.transmit(mic.stream())
    elif command == 'exit':
        exit() # transmitter automatically terminates subprocesses at exit
    else:
        print('Command not recognized!')
