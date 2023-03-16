# sound_sync
Synchronize your Windows audio with your voicemeeter volume.
It works by ckecking if the volume of windows has changed and 
translates the volume to the voicmeeter output.
It also detectes when the volume is detected and mutes voicemeeter if windows
volume gets muted.

Sadly the windows volume only changes in increments of 2, therefore
some volume levels will be skipped in voicemeeter. You can use AutoHotKey
to change the windows volume increments, but it makes it more laggy cause
of the rounding the script does. It still works the same and wont breake.

this readme probably has some issues in it or missing stuff. But most of it is described.
if not  contact me at CoomInPickle#8341 over discord

## Installing
### Preparing voicemeeter
1. click on the vban icon on the top of the voicemeeter window. a new window should pop up
2. in the new window activate vaio with the button in the top left corner
3. enable the last stream in the incoming streams list
4. gather the information needed for the config file wich will be needed later
   - Port       -> found at top middle
   - ip         -> found at top middle
   - streamname -> name of last stream you just activated
   - version    -> top left logo on main window (potato or banana) 
 
### .exe (reccomended)
1. Install the .exe either from releases (if it exists) or just download it as a .zip
2. Put the .exe and the config.txt into a folder and run it.
3. when en error pops up go to the folder where the .py is located and find the config.txt
   (this is normal cause the script doesnt know a target to connect to)
4. Edit the config.txt with the correct information found in the voicemeeter vaio menu.
5. run the .exe again and it should work. if it doesnt check if config.txt if all the information is filled in correctl.

### .py
0. I reccomend using the .exe cause it makes it easyer to run an put into autostart
1. Install the script either from releases (if it exists) or just download it as a .zip
2. Put the script and the config.txt into a folder and run it.
3. when en error pops up go to the folder where the .py is located and find the config.txt
   (this is normal cause the script doesnt know a target to connect to)
5. Edit the config.txt with the correct information found in the voicemeeter vaio menu.
6. run the script again and it should work. if it doesnt check if config.txt if all the information is filled in correctly.

## Autostart
- you can put a shortcut for the .exe into autostart and it will start on startup. just remeber to keep the config.txt and the .exe in the same folder
- for the .py idk how to do, therefore i reccomend the .exe

## Not working?
1. check if the commands arrive in the voicemeeter vban window. if they arrive continue with step 3 otherwhise step 2
2. check if you filled the config.txt file in correctly. if u need a new one just delete the current one and run the script.
   it will generate a new one like the one u donwloaded.
3. check if you have your vban stream configured correctly


## Questions, help or suggestions
- if u cant fix it or you have questions, contact me over discord or leave a comment. (Il probably respond faster on discord)
  - please message me directly with your problem and not just hi and wait until i reply. cause i may wont cause i think you are a bot.
  - try to describe your problem as accurate as possible with the steps u already did
  - please dont spam me and be patient. i also have to to work, therefore i may wont respond instantly. But il try to answer at the same day if possble
  - CoomInPickle#8341
- for suggestions u can also contavt me or leave a comment

# Issues
- Cause of windows volume increments being 2 some volume levels get skipped.
- probably a lot of typos in the readme (tell me if u find some XD)
