from sense_hat import SenseHat
import os
import time
from time import sleep

sense = matrix = SenseHat()

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
maggi_pixels_03 = [
    bk, bk, bk, bk, bk, bk, bk, bk,
    bk, bk, yo, bl, bl, yo, bk, bk,
    bk, yo, yo, yo, yo, yo, yo, bk,
    bk, br, yo, yo, bk, yo, bk, bk,
    bk, yo, yo, yo, yo, yo, rd, rd,
    bk, bk, br, yo, yo, yo, rd, rd,
    bl, bl, bl, bk, bl, bk, bk, bk,
    bl, bl, br, bl, bl, br, bk, bk
]

maggi_pixels_04 = [
    bk, bk, bk, bk, bk, bk, bk, bk,
    bk, bk, yo, bl, bl, yo, bk, bk,
    bk, yo, yo, yo, yo, yo, yo, bk,
    bk, br, yo, yo, bk, yo, bk, bk,
    bk, yo, yo, yo, yo, rd, rd, bk,
    bk, bk, br, yo, yo, rd, rd, bk,
    bl, bl, bl, bk, bl, bk, bk, bk,
    bl, bl, bl, br, bl, bk, bk, bk
]
matrix.clear()
#
#
#while True:  
#  fps_tm = 0.125  
#  matrix.set_pixels(maggi_pixels_01)
#  time.sleep(fps_tm)
#  matrix.set_pixels(maggi_pixels_02)
#  time.sleep(fps_tm)
#  matrix.set_pixels(maggi_pixels_03)
#  time.sleep(fps_tm)
#  matrix.set_pixels(maggi_pixels_04)
#  time.sleep(fps_tm)  
#  matrix.set_pixels(maggi_pixels_03)
#  time.sleep(fps_tm)
#  matrix.set_pixels(maggi_pixels_04)
#  time.sleep(fps_tm)
  