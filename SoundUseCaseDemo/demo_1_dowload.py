"""
    This demo uses simpleaudio library like the name suggests it is realy simple
    just pick a audio file to play then you start and stop the audio file as you
    like. Also there is a check if the file is playing and wait until done. 

    - downside to this is that you dont get to controll the volume of file
"""

import simpleaudio as sa
import time

dowload_compleate_wave_object = sa.WaveObject.from_wave_file(r"resources\voice_male_says_success.wav")
dowload_wave_object = sa.WaveObject.from_wave_file(r"resources\download_click_sound_30.wav")

def execute_demo1():
    i = 0
    play_dowlaod_sound = dowload_wave_object.play()

    if play_dowlaod_sound.is_playing():
        while True:
            i += 1
            # Sleep to imitate download
            time.sleep(.05)
            print('{}%'.format(i), end='\r')

            if(i == 100):
                play_dowlaod_sound.stop()
                play_dowlaod_compleate_sound = dowload_compleate_wave_object.play()
                play_dowlaod_compleate_sound.wait_done()
                break
