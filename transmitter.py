from settings import transmitter as settings
from processes import create
import os


command = 'sudo ' + settings.program_path + ' -f ' + str(settings.frequency) + ' -'


def transmit(stream):
    '''
    Can be called multiple times
    Automatically terminates unnecessary subprocesses
    '''
    return create('transmitter', command, stdin=stream.stdout, stdout=open(os.devnull, 'w'))
