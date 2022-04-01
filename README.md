# talon_command_clipboard
Imitates the functionality of windows clipboard history for repeating talon commands.

# Installation
Assumes you already have Talon Voice: https://talonvoice.com/

Clone or copy this entire repo into the user/ directory of your talon installation. 

# Examples
Say a talon command such as:
'sentence the quick brown fox jumps over the lazy dog'

Optionally say a few other commands.

Opened the command clipboard by saying:
'command clipboard'

Choose the command you would like to repeat either by clicking on it in the list or with the clip command (the word 'clip' followed by the number of your choice):
'clip one'

The command will be repeated once, and can be repeated further using your normal repetition commands now that it is the most recent command.

There is also a command to close the clipboard early:
'command clipboard close'

# Working Items
Ignore duplicate commands?

It causes a recursion error when we try to repeat a clip command, we either need a work around or way to filter them from the list