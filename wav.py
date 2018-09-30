from settings import wav as settings
import subprocess


command = 'sox ' + settings.audio_directory + 'FILENAME.wav -t wav -'


def stream(filename=settings.default_filename):
    return subprocess.Popen(command.replace('FILENAME', filename).split(), stdout=subprocess.PIPE)
