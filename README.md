# sound_sync
Synchronize your Windows audio with your voicemeeter volume.
It works by ckecking if the volume of windows has changed and 
translates the volume to the voicmeeter output.

sadly the windows volume only changes in increments of 2, therefore
some volume levels will be skipped in voicemeeter. You can use AutoHotKey
to change the windows volume increments, but it makes it more laggy cause
of the rounding the script does. It still works the same and wont breake.

##Installing
#.py
yes
@.exe
also yes
