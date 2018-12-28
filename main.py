#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import subprocess

def LEDon():
    """on led"""
    led_cmd = "echo 1 > /dev/myled0"
    subprocess.call(led_cmd, shell=True)

def LEDoff():
    """off led"""
    led_cmd = "echo 0 > /dev/myled0"
    subprocess.call(led_cmd, shell=True)

def wait(self):
    """wait time"""
    time.sleep(self)

def happynewyear():
    #happy
    LEDon()
    wait(0.1)
    LEDoff()
    wait(0.1)

    LEDon()
    wait(0.1)
    LEDoff()
    wait(0.1)
    
    LEDon()
    wait(0.1)
    LEDoff()
    wait(0.1)
   
    LEDon()
    wait(0.1)
    LEDoff()
    wait(0.5)
 
    LEDon()
    wait(0.1)
    LEDoff()
    wait(0.1)

    LEDon()
    wait(0.5)
    LEDoff()
    wait(0.5)
    
    LEDon()
    wait(0.1)
    LEDoff()
    wait(0.1)

    LEDon()
    wait(0.5)
    LEDoff()
    wait(0.1)

    LEDon()
    wait(0.5)
    LEDoff()
    wait(0.1)

    LEDon()
    wait(0.1)
    LEDoff()
    wait(0.5)

    LEDon()
    wait(0.1)
    LEDoff()
    wait(0.1)

    LEDon()
    wait(0.5)
    LEDoff()
    wait(0.1)

    LEDon()
    wait(0.5)
    LEDoff()
    wait(0.1)

    LEDon()
    wait(0.1)
    LEDoff()
    wait(0.5)

    LEDon()
    wait(0.5)
    LEDoff()
    wait(0.1)

    LEDon()
    wait(0.1)
    LEDoff()
    wait(0.1)

    LEDon()
    wait(0.5)
    LEDoff()
    wait(0.1)

    LEDon()
    wait(0.5)
    LEDoff()
    wait(0.1)

#new
    LEDon()
    wait(0.5)
    LEDoff()
    wait(0.1)

    LEDon()
    wait(0.1)
    LEDoff()
    wait(0.5)

    LEDon()
    wait(0.1)
    LEDoff()
    wait(0.5)

    LEDon()
    wait(0.1)
    LEDoff()
    wait(0.1)

    LEDon()
    wait(0.5)
    LEDoff()
    wait(0.1)

    LEDon()
    wait(0.5)
    LEDoff()
    wait(0.1)

#year    
    LEDon()
    wait(0.5)
    LEDoff()
    wait(0.1)
    
    LEDon()
    wait(0.1)
    LEDoff()
    wait(0.1)

    LEDon()
    wait(0.5)
    LEDoff()
    wait(0.1)
    
    LEDon()
    wait(0.5)
    LEDoff()
    wait(0.5)
    
    LEDon()
    wait(0.1)
    LEDoff()
    wait(0.5)

    LEDon()
    wait(0.1)
    LEDoff()
    wait(0.1)

    LEDon()
    wait(0.5)
    LEDoff()
    wait(0.5)

    LEDon()
    wait(0.1)
    LEDoff()
    wait(0.1)

    LEDon()
    wait(0.5)
    LEDoff()
    wait(0.1)

    LEDon()
    wait(0.1)
    LEDoff()

def main():
	happynewyear()
		
if __name__ == "__main__":
	main()
