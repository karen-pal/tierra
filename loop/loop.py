#!/usr/bin/env python3
import mpv

def my_log(loglevel, component, message):
    print('[{}] {}: {}'.format(loglevel, component, message))

player = mpv.MPV(log_handler=my_log, ytdl=False, input_default_bindings=True, input_vo_keyboard=True)

# Property access, these can be changed at runtime
@player.property_observer('time-pos')
def time_observer(_name, value):
    # Here, _value is either None if nothing is playing or a float containing
    # fractional seconds since the beginning of the file.
    if value:
        print('Now playing at {:.2f}s'.format(value))

player.fullscreen = False
player.loop_playlist = 'inf'
# Option access, in general these require the core to reinitialize
player['vo'] = 'gpu'

@player.on_key_press('q')
def my_q_binding():
    print('THERE IS NO ESCAPE')

@player.on_key_press('s')
def my_s_binding():
    pillow_img = player.screenshot_raw()
    pillow_img.save('screenshot.png')

player.play('../tierras/pampa1.mp4')
player.wait_for_playback()
player.wait_for_property('idle-active')
del player
