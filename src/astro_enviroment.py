from sense_hat import SenseHat
from time import sleep
import time

    
last_millis = int(0)
time_period = 1000 # 1 = 1 millsec , 1000 = 1 sec
sense = SenseHat()
humidity = sense.get_humidity()
pressure = sense.get_pressure()
temp = sense.get_temperature()

# Define some colours
tan = tn = (255,222,173)
brown  = br = (139,69,19)
red = rd =(255, 0, 0)
blue = bl =(0, 0, 255)
green = gr = (0, 255, 0)
white = wh =(255, 255, 255)
yellow = yo =(255, 255, 0)
black = bk = (0, 0, 0)
# Set up where each colour will display


creeper_pixels = [
    gr, gr, gr, gr, gr, gr, gr, gr,
    gr, gr, gr, gr, gr, gr, gr, gr,
    gr, bk, bk, gr, gr, bk, bk, gr,
    gr, bk, bk, gr, gr, bk, bk, gr,
    gr, gr, gr, bk, bk, gr, gr, gr,
    gr, gr, bk, bk, bk, bk, gr, gr,
    gr, gr, bk, bk, bk, bk, gr, gr,
    gr, gr, bk, gr, gr, bk, gr, gr
]


mario_pixels = [
    bk, bk, bk, rd, rd, rd, wh, bk,
    bk, bk, rd, rd, rd, rd, rd, rd,
    bk, bk, br, tn, br, bk, tn, bk,
    bk, bk, br, tn, tn, br, br, tn,
    bk, bk, bk, br, tn, tn, tn, bk,
    bk, rd, rd, yo, bl, bl, yo, bk,
    wh, bk, bl, bl, bl, bl, bk, wh,
    bk, bk, yo, bk, bk, bk, yo, bk
]


maggi_pixels_01 = [
    bk, bk, bk, bk, bk, bk, bk, bk,
    bk, bk, yo, bl, bl, yo, bk, bk,
    bk, yo, yo, yo, yo, yo, yo, bk,
    bk, br, yo, yo, bk, yo, bk, bk,
    bk, yo, yo, yo, yo, rd, rd, bk,
    bk, bk, br, yo, yo, rd, rd, bk,
    bl, bl, bl, bk, bl, bk, bk, bk,
    bl, bl, br, bl, bl, br, bk, bk
]

maggi_pixels_02 = [
    bk, bk, bk, bk, bk, bk, bk, bk,
    bk, bk, yo, bl, bl, yo, bk, bk,
    bk, yo, yo, yo, yo, yo, yo, bk,
    bk, br, yo, yo, bk, yo, bk, bk,
    bk, yo, yo, yo, yo, rd, rd, bk,
    bk, bk, br, yo, yo, rd, rd, bk,
    bl, bl, bl, bk, bl, bk, bk, bk,
    bl, bl, bl, br, bl, bk, bk, bk
]

# Take readings from all three sensors
t = sense.get_temperature() 
f = ( t * 1.8 ) + 32
p = sense.get_pressure()
h = sense.get_humidity()

# Round the values to one decimal place
t = round(t, 1)
f = round(f, 1)
p = round(p, 1)
h = round(h, 1)
  
# Create the message
temperature = str(f) + "F "
humidity = str(h) + "% "
pressure = str(p) +"hp"

#while True:
#  sense.show_message(message, scroll_speed=0.1 , text_colour=green)
#  sense.set_pixels(creeper_pixels)
#  sleep(2)