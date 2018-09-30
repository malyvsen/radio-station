import subprocess
import atexit


processes = {}


def create(name, command, kill_target=None, **kwargs):
    '''Create a subprocess, and oversee its predecessor's termination'''
    terminate(name, kill_target)
    processes[name] = subprocess.Popen(command.split(), **kwargs)
    return processes[name]


def terminate(name, kill_target=None):
    if name not in processes:
        return
    if kill_target is None:
        subprocess.call(('sudo', 'kill', str(processes[name].pid)))
    else:
        # processes launched with sudo need to be terminated with their own name
        subprocess.call(('sudo', 'pkill', kill_target))
    del processes[name]


def terminate_all():
    for name in list(processes):
        terminate(name)


atexit.register(terminate_all)
