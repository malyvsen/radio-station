import subprocess
import atexit


processes = {}


def create(name, command, **kwargs):
    terminate(name)
    processes[name] = subprocess.Popen(command.split(), **kwargs)
    return processes[name]


def terminate(name):
    if name not in processes:
        return
    subprocess.call(('sudo', 'kill', str(processes[name].pid)))
    del processes[name]


def terminate_all():
    for name in list(processes):
        terminate(name)


atexit.register(terminate_all)
