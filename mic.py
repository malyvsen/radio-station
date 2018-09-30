from settings import mic as settings
import subprocess


command = 'arecord -D hw:1,0 -c1 -d 0 -r ' + str(settings.sample_rate) + ' -f S16_LE'


def stream():
    return subprocess.Popen(command.split(), stdout=subprocess.PIPE)
