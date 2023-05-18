'''
Counts up and down and plays sound at the end of each lap.
'''

def on_forever():
    count_up(250, 5)
    count_down(250, 5)

basic.forever(on_forever)

def count_up(delay = 200, to = 10):
    for i in range(to):
        basic.show_number(i)
        basic.clear_screen()
        basic.pause(delay)
    play_sound()

def count_down(delay = 200, count = 9):
    while (count >= 0):
        basic.show_number(count)
        basic.clear_screen()
        basic.pause(delay)
        count = count - 1

def play_sound():
    music.play_sound_effect(
        music.create_sound_effect(
            WaveShape.SINE,
            5000,
            0,
            255,
            0,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR
        ),
        SoundExpressionPlayMode.UNTIL_DONE
    )
