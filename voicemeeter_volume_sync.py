import configparser
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import vban_cmd
import os

config_file = os.path.exists(r"./config.txt")
if config_file == False:
    with open("config.txt", "w") as file:
        file.write("# enter your vban stuff in here         \n")
        file.write("# by replacing all the capitalized words\n")
        file.write("# with the corresponding information.   \n")
        file.write("                                        \n")
        file.write("[vban_connection]                       \n")
        file.write("port = PORT                             \n")
        file.write("ip = IP                                 \n")
        file.write("streamname = Streamname                 \n")
        file.write("version = VERSION                       \n")


# config file stuff
config = configparser.ConfigParser()
config.read_file(open(r'config.txt'))


# getting the config info
cport = config.get("vban_connection", "port")
cip = config.get("vban_connection", "ip")
cstreamname = config.get("vban_connection", "streamname")
cversion = config.get("vban_connection", "version")


# audio stuff
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
current_volume = volume.GetMasterVolumeLevel()


# voicemeeter stuff
vban = vban_cmd.api(cversion, ip=cip, port=int(cport), streamname=cstreamname)


# commands for diffrent apps
class potato:
    def __init__(self, vban):
        self.vban = vban

    def volume(self):
        self.vban.strip[5].gain = sync_vol()
        self.vban.strip[6].gain = sync_vol()
        self.vban.strip[7].gain = sync_vol()

    def mute(self):
        self.vban.strip[5].mute = old_mute
        self.vban.strip[6].mute = old_mute
        self.vban.strip[7].mute = old_mute


class banana:
    def __init__(self, vban):
        self.vban = vban

    def volume(self):
        self.vban.strip[3].gain = sync_vol()
        self.vban.strip[4].gain = sync_vol()

    def mute(self):
        self.vban.strip[3].mute = old_mute
        self.vban.strip[4].mute = old_mute


banana = banana(vban)
potato = potato(vban)


# getting values for volume
def sync_vol():
    wvolme = round(volume.GetMasterVolumeLevelScalar() * 100)
    vmvolume = round(wvolme * +0.72 - 60)
    return vmvolume


# getting starting state of volume and mute
old_vol = volume.GetMasterVolumeLevelScalar()
old_mute = volume.GetMute()


# actual synchonizing
if cversion == "potato":  # for potato
    while True:
        new_vol = volume.GetMasterVolumeLevelScalar()
        if old_vol != new_vol:
            old_vol = new_vol
            potato.volume()

        new_mute = volume.GetMute()
        if old_mute != new_mute:
            old_mute = new_mute
            potato.mute()

elif cversion == "banana":  # for banana
    while True:
        new_vol = volume.GetMasterVolumeLevelScalar()
        if old_vol != new_vol:
            old_vol = new_vol
            banana.volume()

        new_mute = volume.GetMute()
        if old_mute != new_mute:
            old_mute = new_mute
            banana.mute()
