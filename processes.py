import subprocess
import atexit


processes = {}


def create(name, command, **kwargs):
    '''Create a subprocess, and oversee its predecessor's termination'''
    terminate(name, kill_target)
    processes[name] = subprocess.Popen(command.split(), **kwargs)
    return processes[name]


def terminate(name):
    if name not in processes:
        return
    if processes[name].args[0] == 'sudo':
        # processes launched with sudo need to be terminated with their own name
        subprocess.call(('sudo', 'pkill', processes[name].args[1]))
    else:
        subprocess.call(('sudo', 'kill', str(processes[name].pid)))
    del processes[name]


def terminate_all():
    for name in list(processes):
        terminate(name)


atexit.register(terminate_all)
