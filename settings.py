import os


class transmitter:
    frequency = 100 # in MHz
    program_name = 'fm_transmitter'
    program_path = os.path.join(os.path.dirname(__file__), 'fm_transmitter/' + program_name)


class wav:
    audio_directory = os.path.join(os.path.dirname(__file__), 'audio/')
    default_filename = 'default'


class mic:
    sample_rate = 24000
