from settings import transmitter as settings
import subprocess
import atexit


command = 'sudo ' + settings.program_path + ' -f ' + str(settings.frequency) + ' -'


def transmit(stream):
    '''
    Can be called multiple times
    Automatically terminates unnecessary subprocesses
    '''
    terminate()
    global current_stream, current_transmission
    current_stream = stream
    current_transmission = subprocess.Popen(command.split(), stdin=stream.stdout)


current_stream = None
current_transmission = None


def terminate():
    global current_stream, current_transmission
    if current_stream is not None:
        current_stream.terminate()
    if current_transmission is not None:
        current_transmission.terminate()


atexit.register(terminate)
