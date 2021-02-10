from pyo import *
import time, os, sys, platform

"""
    Checks the operation system that you are running on
    determines the right console clean command for 
    command line
"""

def clean_terminal():
    if platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Darwin':
        os.system('clear')

def execute_demo2():

    # This is the audio controlling part
    s = Server(sr=96000, nchnls=1, buffersize=128, duplex=1).boot()

    # path + audio files used
    folder = "resources\premium_beat_aiff\\"
    sounds = ["PremiumBeat_0013_cursor_selection_15.aiff", "PremiumBeat_0013_move_cursor_11.aiff"]
    
    s.start()
    sounds_to_play = SfPlayer(folder + sounds[0], speed=1, mul=0.5).out()

    # Clean slate
    clean_terminal()

    welcome = "Systems starting up"
    good_bye = "Systems shutting down"

    
    i = 0
    while True:
        
        # This line is mvp. It is not so simple to print to same line in windows
        # that you would imagine
        print(welcome.ljust(os.get_terminal_size().columns - 1), end="\r")
        time.sleep(1)

        if welcome == "Systems starting up...":
            welcome = welcome[:-3]
        else:
            welcome = welcome + '.'
            i += 1
        
        if i == 9:
            clean_terminal()
            break

    # Swiching the audio file to other sound
    sounds_to_play.setPath(folder + sounds[1])
    
    # Programming is up and running and user dose his thing
    print('\n ---------- \n Program runs and starts shutdown \n ---------- \n')
    time.sleep(3)

    clean_terminal()

    # System shutdown text loop and a sound to go with it(0013 move cursor 11)
    sounds_to_play.out()

    x = 0
    while True:
        
        print(good_bye.ljust(os.get_terminal_size().columns - 1), end="\r")
        time.sleep(1)

        if good_bye == "Systems shutting down...":
            good_bye = good_bye[:-3]
        else:
            good_bye = good_bye + '.'
            x += 1
        
        if x == 9:
            clean_terminal()
            break

