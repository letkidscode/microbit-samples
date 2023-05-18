'''
When you press button A or B, a slightly different sound is
produced and a random number between 0 and 10 is displayed
on the LED.
'''

def play_sound(x = 5000):
    music.play_sound_effect(
        music.create_sound_effect(
            WaveShape.SINE,
            x,
            0,
            255,
            0,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR
        ),
        SoundExpressionPlayMode.UNTIL_DONE
    )

def get_number():
    return Math.floor(Math.random() * 10)

def on_button_pressed_a():
    play_sound(8000)
    num = get_number()
    basic.show_number(num)

def on_button_pressed_b():
    play_sound()
    num = get_number()
    basic.show_number(num)

input.on_button_pressed(Button.A, on_button_pressed_a)

input.on_button_pressed(Button.B, on_button_pressed_b)
