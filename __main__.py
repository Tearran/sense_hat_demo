from src.astro_enviroment import *
import os
import time


while True: 
  os.system('cls||clear')
  
  print("____menu_____")
  print(" ")
  print("1: Display Temprature\n")
  print("2: Display Humidity\n")
  print("3: Display Pressure\n")
  print("4: Display Creeper\n")
  print("5: Display Mario\n")
  print("6: Display Maggi\n")
  print("7: Display a Blank\n")
  print("8: Display a Demo loop\n")
  print("9: Clear display\n")
  print("0: Exit\n")

  ch = int(input())

  if ch == 1:
    sense.clear()
    print( temperature )
    sense.show_message( temperature, scroll_speed=0.1 , text_colour=green )

  if ch == 2:
    print( humidity )
    sense.show_message( humidity, scroll_speed=0.1 , text_colour=green )

  if ch == 3:
    sense.clear()
    print( pressure )
    sense.show_message( pressure, scroll_speed=0.1 , text_colour=green )

  if ch == 4:
    sense.clear()  
    sense.set_pixels(creeper_pixels)

  if ch == 5:
    sense.clear()    
    sense.set_pixels(mario_pixels)
  
  if ch == 6: 
    sense.clear()
    while True:
      fps_tm = 0.25  
      sense.set_pixels(maggi_pixels_01)
      time.sleep(fps_tm)
      sense.set_pixels(maggi_pixels_02)
      time.sleep(fps_tm)

      
  if ch == 7:
    sense.clear()
    sense.set_pixels(mario_pixels)
    
  if ch == 8:
    sense.clear()
    sense.set_pixels(creeper_pixels)

  if ch == 7 :
    sense.clear()

  if ch == 8 :
    while True:
      sense.clear()
      sense.show_message(temperature, scroll_speed=0.125 , text_colour=green)
      sense.set_pixels(creeper_pixels)
      do_somthing()
      sense.show_message(humidity, scroll_speed=0.125 , text_colour=green)
      sense.set_pixels(mario_pixels)
      time.sleep(1)
      sense.show_message( pressure, scroll_speed=0.125 , text_colour=green )
      sense.set_pixels(maggi_pixels)
      time.sleep(1)


  if ch == 9 :
    sense.clear()

  if ch == 0:
    quit()
  
    exit(0)
    