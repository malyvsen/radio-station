import os


class transmitter:
    frequency = 100 # in MHz
    program_name = 'fm_transmitter'
    program_path = os.path.join(os.path.dirname(__file__), 'fm_transmitter/' + program_name)


class wav:
    audio_directory = os.path.join(os.path.dirname(__file__), 'audio/')


class mic:
    sample_rate = 48000 # in Hz


class silence:
    sample_rate = 44100 # in Hz
