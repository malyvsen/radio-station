# radio-station
Minimalistic command-line interface for streaming audio over FM from a Raspberry Pi: WAV files or live from a microphone.

## Setup
### Clone into the repository  
```sh
git clone https://github.com/malyvsen/radio-station.git
cd radio-station
```
### Prepare fm_transmitter
This project uses fm_transmitter from https://github.com/markondej/fm_transmitter
```sh
git submodule update --init --recursive
cd fm_transmitter
make
cd ..
```
### Add an antenna
The broadcaster works without an antenna, but adding one significantly improves the range (from 50cm to 10m on a Raspberry Pi 2). Connect 10-20cm of wire to GPIO4.

## Usage
### Broadcast
```sh
cd .. # you need to be one directory above this repo
sudo python3 radio-station/ # the sudo is necessary to run fm_transmitter
```
The program will display usage instructions. Use `play test` to test your radio with the included test file.
### Configure
The broadcasting frequency and other settings are stored in `settings.py`. You will need to restart your station for settings to be applied.
### Legal
Make sure you are allowed to use the frequency you set - you are the only one responsible for your radio station.
