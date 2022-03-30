from typing import List, Optional
from talon import actions, Module, speech_system, imgui

mod = Module()

command_clipboard = []
MAX_LENGTH = 10

@imgui.open(y=0, x=0)
def gui(gui: imgui.GUI):
    global command_clipboard
    gui.text("Command Clipboard")
    gui.line()
    for command in command_clipboard:
        text = actions.user.history_transform_phrase_text(command)
        if text is not None and gui.button(text):
            actions.user.command_clipboard_repeat(command)
            actions.user.command_clipboard_disable()



def fn(d):
    if "parsed" not in d: return
    actions.user.history_append_command(d["parsed"]._unmapped)


speech_system.register("pre:phrase", fn)


@mod.action_class
class Actions:
    def command_clipboard_toggle():
        """Toggles viewing the command clipboard"""
        if gui.showing:
            gui.hide()
        else:
            gui.show()

    def command_clipboard_disable():
        """Disables the command clipboard"""
        gui.hide()

    def command_clipboard_repeat(words: List[str]):
        """Repeat the chosen command"""
        actions.mimic(words)

    def history_append_command(words: List[str]):
        """Appends a command to the command clipboard; called when a voice command is uttered"""
        command_clipboard.append(words)
        if len(command_clipboard) > MAX_LENGTH:
            command_clipboard.pop(0)
        print(command_clipboard)
