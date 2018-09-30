from settings import wav as settings
from processes import create
import subprocess


command = 'sox ' + settings.audio_directory + 'FILENAME.wav -t wav -'


def stream(filename=settings.default_filename):
    return create('wav', command.replace('FILENAME', filename), stdout=subprocess.PIPE)
