from pyo import *


s = Server(sr=96000, nchnls=1, buffersize=128, duplex=1).boot()

# Sound bank
folder = "resources\premium_beat_aiff\\"
sounds = ["PremiumBeat_0013_cursor_click_01.aiff", "PremiumBeat_0013_cursor_click_06.aiff",
"PremiumBeat_0013_cursor_click_11.aiff", "PremiumBeat_0013_cursor_click_18.aiff",
"PremiumBeat_0013_cursor_click_16.aiff"]

# Creates the left and right players
sfL = SfPlayer(folder + sounds[0], speed=1, mul=0.5).out()

# Function to choose a new sound and a new speed for the left player
def newL():
    r = random.randint(0,3)
    print(r)
    sfL.path = folder + sounds[r]
    sfL.out()


# The "end-of-file" signal triggers the function "newL"
tfL = TrigFunc(sfL["trig"], newL)


s.start()
time.sleep(5)
s.stop()
