from pyo import *
import time, os, sys, platform
import msvcrt as m
import msvcrt as m
import keyboard

# THIS IS A TEST PLATFORM FOR ME TO FUCK A ROUND IN !! NOT FOR PRODUCTION DEMO

# This is the audio controlling part
s = Server(sr=96000, nchnls=1, buffersize=128, duplex=1).boot()

# path + audio files used
folder = "resources\pianoSound\\"
sounds = ["Piano.pp.A1.aiff", "Piano.pp.A2.aiff", "Piano.pp.A3.aiff", "Piano.pp.B0.aiff", 
"Piano.pp.B1.aiff", "Piano.pp.B2.aiff", "Piano.pp.B3.aiff", "Piano.pp.C1.aiff", 
"Piano.pp.C2.aiff", "Piano.pp.C3.aiff", "Piano.pp.C4.aiff", "Piano.pp.D1.aiff", 
"Piano.pp.D2.aiff", "Piano.pp.D3.aiff", "Piano.pp.D4.aiff", "Piano.pp.E1.aiff", 
"Piano.pp.E2.aiff", "Piano.pp.E3.aiff", "Piano.pp.E4.aiff", "Piano.pp.F1.aiff", ]
s.start()
sounds_to_play = SfPlayer(folder + sounds[0], speed=1, mul=0.5)

mix_level = 1

def check_action_for_key(key):
    dict_of_actions = {"a": a_sound, "s": b_sound}
    #print(key)
    sound = dict_of_actions.get(key)
    sound()
    sounds_to_play.out()
    



def a_sound():
    sounds_to_play.setPath(folder + sounds[3])


def b_sound():
    sounds_to_play.setPath(folder + sounds[15])




# This could be one solution for a keypress    
while(True):
    #key_press_bytes = m.getch()
    #key_press = key_press_bytes.decode('utf-8')
    #print(key_press)
    key_press = keyboard.on_release()

    if(keyboard.is_pressed('p') == 'p'):
        break
    else:
        check_action_for_key(key_press)






