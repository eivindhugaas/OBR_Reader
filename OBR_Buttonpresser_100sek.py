#    "OBR_analyzer_simple" (v1.0)
#    Copyright 2016 Soren Heinze
#    soerenheinze <at> gmx <dot> de
#    5B1C 1897 560A EF50 F1EB 2579 2297 FAE4 D9B5 2A35
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


# A small program to automatically press the correct buttons that a proprietary
# OBR-measurement/analyzing program analyzes the OBR rawdata.
# The files will also be saved automatically, assuming that CTRL + S 
# is the shortcut to open the "save-file" dialogue of OBR-measurement program.
# For each analyzes the reference file will be changed.
# 
# This program is a modification of the OBR_buttonpresser_simple.py program.
# It assumes that a "Load Reference File ..." option can be found 70 pixels 
# below the "File" button in the menu bar. 
# This is the case for a certain version of the proprietary 
# OBR-measurement/analyzing program (stated in the accompanying manual to this
# program) for which the OBR_analyzer_simple program was tested for.
# 
#
# I decided to restrict myself to the most basic programming statements 
# (if possible) and NOT to use functions or classes. 
# While I personally don't like this, I hope that this makes it easier for 
# the interested but usually not programming user when she or he does not need 
# to jump to different places or even files while trying to understand what's
# going on here.
import numpy as np
import win32api, win32con
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from time import sleep, time
from Smoothening_Functions.SmootheningFunctions import smoothening as smth
smth=smth()
import os

def click(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


mouse = PyMouse()
keyboard = PyKeyboard()


waittime=100

print """\n
        Move the mouse pointer over the Start Measurement Button.
        
        DON'T click the mouse! 
        The console must remain the active window!
        
        Once this is done, press ENTER (the position of the <FILE> Button will
        be detected).

        """

raw_input('Press ENTER when the mouse is over the <FILE> Button.')

print "\n\n<<<<<<<< <FILE> Button position determined >>>>>>>>"

file_button_position = mouse.position()

load_reference_button_position = (file_button_position[0], (file_button_position[1]))

raw_input('Press ENTER now to start the automatic measurements. >>>')

for i in range(1000000):

	click(load_reference_button_position[0], load_reference_button_position[1])
	sleep(waittime)








