import time
from pixel_maggi_animation import *
from sense_hat import SenseHat
from time import sleep

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
last_millis = int(0)
pixel_fps =  8 # frames per second
time_period = 1000 / pixel_fps # 1000 = 1 sec
sensor_read_count = (temperature, humidity, pressure)
pixel_frame = (maggi_pixels_01, maggi_pixels_02, maggi_pixels_03, maggi_pixels_04)
pixel_frame_count = int(0)

def do_somthing():
  print(sensor_read_count[0])
  print(sensor_read_count[1])
  print(sensor_read_count[2])
  print('\n')

def do_somthing_more(i):
    print(i)

def no_sleep():
  global last_millis
  this_millis = int(time.time()*1000.0) # nanosec to millsec

  if this_millis - last_millis >= time_period:
    last_millis = this_millis

    global pixel_frame_count
    global sensor_read_count
    if pixel_frame_count < 4:
      sense.set_pixels(pixel_frame[pixel_frame_count])
      do_somthing_more(pixel_frame_count)
      pixel_frame_count += 1
    else:
      pixel_frame_count=0
      do_somthing()
      do_somthing_more(time_period)

while True:
  no_sleep()
  sleep(0.0125)
