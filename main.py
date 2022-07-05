def on_button_pressed_a():
    global hours
    if hours < 23:
        hours += 1
    else:
        hours = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global ampm
    ampm = not (ampm)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global minutes
    if minutes < 59:
        minutes += 1
    else:
        minutes = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global time
    time = "" + str(hours) + (":" + str(minutes))
    basic.show_string(time)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

hours = 0
minutes = 0
time = ""
ampm = False
ampm = False
adjust = 0
time = ""
minutes = 0
hours = 0

def on_forever():
    global minutes, hours
    basic.pause(60000)
    if minutes < 59:
        minutes += 1
    else:
        minutes = 0
        if hours < 23:
            hours += 1
        else:
            hours = 0
basic.forever(on_forever)
