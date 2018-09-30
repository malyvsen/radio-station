from settings import mic as settings
from processes import create
import subprocess


command = 'arecord -D hw:1,0 -c1 -d 0 -r ' + str(settings.sample_rate) + ' -f S16_LE'


def stream():
    return create('mic', command, stdout=subprocess.PIPE)
