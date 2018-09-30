from settings import silence as settings
from processes import create
import subprocess


command = 'sox -n -r ' + str(settings.sample_rate) + ' -b 16 -t wav -'


def stream():
    return create('stream', command, stdout=subprocess.PIPE)
