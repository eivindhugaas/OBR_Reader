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

def click(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

# Instantiate a mouse and a keyboard.
# A PyMouse() and a PyKeyboard() have certain methods that allow 
# easy access to typical features of such peripherals like moving the
# pointer to a certain position or pressing keyboard buttons.
mouse = PyMouse()
keyboard = PyKeyboard()


# Just reminding the user of sth. very important.




highest_numbers=np.arange(27,329,12)
start_heres=np.arange(16,317,12)

analysis_time=5
save_time=5
RRef=True
base_filenames=["F_08_fibre 1_","F_08_fibre 2_","F_08_fibre 3_","F_08_fibre 4_"]
#base_filename="F_08_fibre 1_"

# Instructions for the user what to do, so that the program can determine the 
# position of the <FILE> Button
print """\n
        Move the mouse pointer over the <FILE> Button in the MENU BAR of the OBR program.
        
        DON'T click the mouse! 
        The console must remain the active window!
        
        Once this is done, press ENTER (the position of the <FILE> Button will
        be detected).
        
        DON'T MOVE THE WINDOW OF THE OBR-PROGRAM AFTERWARDS!\n
        """


# Using raw_input() I make sure that the program will halt here and wait 
# for ENTER.
raw_input('Press ENTER when the mouse is over the <FILE> Button.')


print "\n\n<<<<<<<< <FILE> Button position determined >>>>>>>>"


# Here the position of the mouse pointer is determined.
# .position() returns a tuple that contains the x- and y-coordinates
# of the pointer at the time this method is called.
file_button_position = mouse.position()
# file_button_position[0] / file_button_position[1] retrieves the first / second 
# entry of the tuple that contains the x- and y-coordinates of the 
# <FILE> Button
load_reference_button_position = (file_button_position[0], (file_button_position[1] + 70))

# Some more information for the user.
print """\n
        ATTENTION: DON'T MOVE THE WINDOW OF THE OBR-PROGRAM
        
        After pressing ENTER again the OBR window will become active and the 
        automatic analysis will start.
        DON'T make this console the active window after pressing ENTER.
        It will work even if you can't see this console.\n
        """


# Wait here for the user to start the automatic measurements.
raw_input('Press ENTER now to start the automatic measurements. >>>')
for base_filename in base_filenames:
	
	#for i in range(0,1000):
		start_here= 1 #start_heres[i]
		highest_number = 428 #highest_numbers[i]
		
		
	
		
		
		# Give the user a summary of the input information.
		print "\n-----------------------\n"
		print "ATTENTION: DON'T MOVE THE WINDOW OF THE OBR-PROGRAM!\n"
		print "Automated Measurements have started.\n"
		print "Highest file number: %s" % highest_number
		print "Starting with measurement: %s" % start_here
		print "Base-filename: %s" % base_filename
		print "\n-----------------------\n"
		
		
		
		
		
		## ## ## ## ## Here the analysis-loop starts ## ## ## ## ##
		
		counter = start_here - 1
		
		while counter < highest_number:
			# Increase the file number counter
			counter += 1
		
			# The numbering of the files should be with four leading zeros but counter 
			# is just a regular number. 
			# .zfill() puts leading zeros in front of a number. However, .zfill() can 
			# be used just on a string. Thus I first convert the number to a string.
			load_file_number = str(counter).zfill(4)
			if RRef:
				new_reference_file_number = str((counter - 1)).zfill(4)
			elif not RRef:
				print('hi')
				new_reference_file_number = str((Refnum)).zfill(4)
			print(new_reference_file_number)
			# Make the correct filename, by concatenating the base-filename and
			# the number for the measurement that is performed.
			load_file = base_filename + load_file_number
			new_reference_file = base_filename + new_reference_file_number
			save_file_older_reference = load_file + '_older_reference'
		
		
			# First of all I need to make the OBR measurement/analyze program
			# the active window. I do this by simply clicking it at a position the 
			# does not contain anything.
			click(load_reference_button_position[0], load_reference_button_position[1])
		
		
			# Load the new file to be analyzed.
			# .press_key() is a method of a PyKeyboard-instance that presses and holds
			# the given key and does NOT release it until release_key() is called.
			# keyboard.control_l_key selects the left CTRL-key
			keyboard.press_key(keyboard.control_l_key)
			# .tap_key() taps the given key.
			keyboard.tap_key('l')
			# Don't forget to release the pressed CTR-key.
			keyboard.release_key(keyboard.control_l_key)
		
			# I put in sleep() statements all over this loop to give the 
			# analysis-PC some time to "settle" between commands.
			sleep(0.8)
		
			keyboard.tap_key(keyboard.return_key)
			sleep(0.8)
			keyboard.tap_key('y')
			sleep(0.8)
			load_filetoluna=load_file + '.obr'
			keyboard.type_string(load_filetoluna)
			sleep(0.8)
			keyboard.tap_key(keyboard.return_key)	
			# It takes some time to analyze the file.
			sleep(analysis_time)
		
			#if RRef:
		
				## Now save the file.
				#keyboard.press_key(keyboard.control_l_key)
				#keyboard.tap_key('s')
				#keyboard.release_key(keyboard.control_l_key)
				#sleep(1)
				## This is the file analyzed with the "older" reference.
				#keyboard.type_string(save_file_older_reference)
				#sleep(1)
				#keyboard.tap_key(keyboard.return_key)
				#sleep(save_time)
		
		
		
			# Load the new reference (which will be the previous measurement file).
			
			click(load_reference_button_position[0], load_reference_button_position[1])
			
			click(file_button_position[0], file_button_position[1])
			sleep(0.8)
			click(load_reference_button_position[0], load_reference_button_position[1])
			keyboard.tap_key(keyboard.return_key)
			sleep(0.8)
			new_reference_filetoluna=new_reference_file + '.obr'
			print(new_reference_filetoluna)
			keyboard.type_string(new_reference_filetoluna)
			sleep(0.8)
			keyboard.tap_key(keyboard.return_key)	
			sleep(0.8)
			# When a reference file is loaded the OBR program opens a popup
			# saying this to the user. It may take some time before this popup
			# appears.
			keyboard.tap_key(keyboard.return_key)
		
			# The loaded file will now be analyzed with the new reference.
			sleep(analysis_time)
		
			# And save this file, too.
			keyboard.press_key(keyboard.control_l_key)
			keyboard.tap_key('s')
			keyboard.release_key(keyboard.control_l_key)
		
			sleep(0.8)
			keyboard.type_string(load_file)
			sleep(0.8)
			keyboard.tap_key(keyboard.return_key)
			sleep(save_time)
		
			print "Analyzed %s" % load_file
		
			# To give the user some time to abort the program.
			sleep(0.8)
	
	
	
	
	
	
	


