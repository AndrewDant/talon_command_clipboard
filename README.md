# talon_command_clipboard
Imitates the functionality of windows clipboard history for repeating talon commands. Can also be used as an alternate form of command history, or to easily repeat multiple commands.

# Installation
Assumes you already have Talon Voice: https://talonvoice.com/

Clone or copy this entire repo into the user/ directory of your talon installation. 

# Examples
Say a talon command such as:
`sentence the quick brown fox jumps over the lazy dog`

Optionally say a few other commands.

Opened the command clipboard by saying:

`command clipboard`

Choose the command you would like to repeat either by clicking on it in the list or with the clip command (the word 'clip' followed by the number of your choice):

`clip one`

The command will be repeated once, and can be repeated further using your normal repetition commands now that it is the most recent command.

There is also a command to close the clipboard early:
`command clipboard close`

You can repeat a range of commands using 'range clip <number_small> to <number_small>'

`range clip three to five`

You can repeat any number of clipped commands using 'multi clip <number_small> (and <number_small>)*'. This include repeating the same command multiple times by saying the same number multiple times.

`multi clip one and one and three and four and seven`

You can save any number of clipped commands into a macro to repeat later using 'macro clip <number_small> (and <number_small>)*'. This include repeating the same command multiple times by saying the same number multiple times.

`macro clip one and five and one and eight`

Play a saved macro (repeating each saved command) using 'clip macro [play]'

`clip macro`

# Settings
You can use the following settings to customize how this tool functions. You can refer to the unofficial talon wiki for how [talon settings](https://talon.wiki/unofficial_talon_docs/#settings) work.
- `command_clipboard_max_length` the maximum number of items to record and display in the command clipboard
- `command_clipboard_y_position` the y position of where to display the clipboard. 0 (the default) is the top of the screen
- `command_clipboard_x_position` the x position of where to display the clipboard. 0 (the default) is the far left of the screen
- `command_clipboard_auto_close` whether or not the clipboard should automatically close when a command is selected. 0 for false, any other number for true

# Limitations
You cannot repeat a 'clip' command

# Working Items
Ignore duplicate commands?

It causes a recursion error when we try to repeat a clip command, we either need a work around or to filter them from the list