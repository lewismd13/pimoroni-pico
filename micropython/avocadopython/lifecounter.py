from dis import dis
import time
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY2, PEN_P8

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY2, pen_type=PEN_P8, rotate=0)

display.set_backlight(0.5)
display.set_font("gothic")

# not sure what to use this for yet
button_a = Button(12)
# use b for reset total
button_b = Button(13)
# use x for life up
button_x = Button(14)
# use y for life down
button_y = Button(15)

WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
CYAN = display.create_pen(0, 255, 255)
MAGENTA = display.create_pen(255, 0, 255)
YELLOW = display.create_pen(255, 255, 0)
GREEN = display.create_pen(0, 255, 0)
RED = display.create_pen(255, 0, 0)

# sets up a handy function we can call to clear the screen
def clear():
    display.set_pen(BLACK)
    display.clear()
    display.update()


# set up
clear()

lifetotal = 40

while True:
    # change the color based on life total
    if lifetotal >= 25:
        display.set_pen(GREEN)
    elif lifetotal >= 10:
        display.set_pen(YELLOW)
    elif lifetotal < 10:
        display.set_pen(RED)

    display.text(lifetotal, 5, 5, scale=4)
    display.update()
    
    # reset life total to 40 by default. if it's already 40, make it 20 for non-edh
    if button_b.read():
        if lifetotal == 40:
            lifetotal = 20
        else:
            lifetotal = 40

    # x button is gain a life
    elif button_x.read():
        lifetotal+=1

    # y button is lose a life
    elif button_y.read():
        lifetotal-=1


