from typing import List, Optional
from talon import actions, Module, speech_system, imgui
from typing import Dict
import time

mod = Module()

@mod.capture(rule="[slow] <number_small>")
def clip_number(m) -> str:
    return {
        "slow": "slow" in m,
        "number": m.number_small
    }

@mod.capture(rule="<clip_number> | <clip_number> to <clip_number>")
def clip_range(m) -> str:
    clip_numbers = m.clip_number_list
    if not "to" in m:
        return clip_numbers[0]

@mod.capture(rule="<clip_number> (and <user.>)*")
def clip_set(m) -> dict:
    return m.clip_number_list

command_clipboard = []
macro = []

setting_max_length = mod.setting(
    "command_clipboard_max_length",
    type=int,
    default=10,
    desc="the maximum number of items to record and display in the command clipboard",
)

setting_y_position = mod.setting(
    "command_clipboard_y_position",
    type=int,
    default=0,
    desc="the y position of where to display the clipboard. 0 (the default) is the top of the screen",
)

setting_x_position = mod.setting(
    "command_clipboard_x_position",
    type=int,
    default=0,
    desc="the x position of where to display the clipboard. 0 (the default) is the far left of the screen",
)

setting_auto_close = mod.setting(
    "command_clipboard_auto_close",
    type=int,
    default=1,
    desc="whether or not the clipboard should automatically close when a command is selected. 0 for false, any other number for true",
)

@imgui.open(y=setting_y_position.get(), x=setting_x_position.get())
def gui(gui: imgui.GUI):
    global command_clipboard
    gui.text("Command Clipboard")
    gui.line()
    index = 0
    for command in command_clipboard:
        text = actions.user.command_clipboard_transform_phrase_text(command)
        index += 1
        if text is not None and gui.button('{}. {}'.format(index, text)):
            actions.user.command_clipboard_repeat_command(command)
            if setting_auto_close.get():
                actions.user.command_clipboard_disable()
                
@imgui.open(y=0, x=0)
def macro_gui(gui: imgui.GUI):
    global macro
    gui.text("Macro commands:")
    gui.line()
    index = 0
    for command in macro:
        text = actions.user.command_clipboard_transform_phrase_text(command["command"])
        index += 1
        if text is not None and gui.button('{}. {}'.format(index, text)):
            actions.user.command_clipboard_repeat_command(command["command"])
            if setting_auto_close.get():
                actions.user.command_clipboard_disable()


def fn(d):
    if "text" not in d or not actions.speech.enabled(): return
    actions.user.history_append_command(d["text"])


speech_system.register("pre:phrase", fn)


@mod.action_class
class Actions:
    def command_clipboard_disable():
        """Disables the command clipboard"""
        gui.hide()

    def command_clipboard_toggle():
        """Toggles viewing the command clipboard"""
        if gui.showing:
            gui.hide()
        else:
            gui.show()
            
    def command_clipboard_toggle_macro_gui():
        """Toggles viewing the macro gui"""
        if macro_gui.showing:
            macro_gui.hide()
        else:
            macro_gui.show()

    def command_clipboard_repeat_command(words: List[str]):
        """Repeat the chosen command"""
        actions.mimic(words)

    def command_clipboard_repeat_range(range_start: int, range_end: int):
        """Repeat a range of commands from the clipboard"""
        if 0 < range_start < len(command_clipboard) and 0 < range_end < len(command_clipboard):
            if range_start > range_end:
                temporary_array = command_clipboard[range_end:range_start + 1]
                temporary_array.reverse()
            else:
                temporary_array = command_clipboard[range_start:range_end + 1]
            
            for command in temporary_array:
                actions.user.command_clipboard_repeat_command(command)
                
    def command_clipboard_repeat_multi(clip_list: list[dict[str, int]]):
        """Repeat one or more commands from the clipboard in the order that they were given"""
        if all(0 < clip["number"] < len(command_clipboard) for clip in clip_list):
            command_list = [ { "slow": clip["slow"], "command": command_clipboard[clip["number"]] } for clip in clip_list]
            for command in command_list:
                if command["slow"]:
                    time.sleep(0.5)
                actions.user.command_clipboard_repeat_command(command["command"])
            if setting_auto_close.get():
                actions.user.command_clipboard_disable()
    
    def command_clipboard_update_macro(clip_list: list[dict[str, int]]):
        """Add one or more commands from the clipboard to the end of the macro"""
        global macro
        if all(0 < clip["number"] < len(command_clipboard) for clip in clip_list):
            macro += [ { "slow": clip["slow"], "command": command_clipboard[clip["number"]] } for clip in clip_list]
    
    def command_clipboard_trim_macro(number_list: list[int]):
        """Remove one or more commands from the macro by their macro index"""
        global macro
        if all(0 < index < len(macro) for index in number_list):
            macro = [command for index, command in enumerate(macro) if index not in number_list]
            
    def command_clipboard_reset_macro():
        """Clear all commands from the macro"""
        global macro
        macro = []

    def command_clipboard_play_macro():
        """Replay the recorded macro"""
        for command in macro:
            if command["slow"]:
                    time.sleep(0.5)
            actions.user.command_clipboard_repeat_command(command["command"])

    def history_append_command(words: List[str]):
        """Appends a command to the command clipboard; called when a voice command is uttered"""
        command_clipboard.insert(0, words)
        if len(command_clipboard) > setting_max_length.get():
            command_clipboard.pop()

    def command_clipboard_transform_phrase_text(words: list[str]) -> Optional[str]:
        """Transforms phrase text for presentation in command clipboard. Return `None` to omit from history"""

        return ' '.join(words) if words else None
