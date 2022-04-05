from typing import List, Optional
from talon import actions, Module, speech_system, imgui

mod = Module()

command_clipboard = []

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
    type=bool,
    default=True,
    desc="whether or not the clipboard should automatically close when a command is selected",
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

    def command_clipboard_repeat_command(words: List[str]):
        """Repeat the chosen command"""
        actions.mimic(words)

    def command_clipboard_repeat_number(number: int):
        """Repeat the command with the specified number"""
        if 0 < number < len(command_clipboard):
            # we don't subtract one from the number to get the index because the clip command becomes the new index 0
            actions.user.command_clipboard_repeat_command(command_clipboard[number])
            if setting_auto_close.get():
                actions.user.command_clipboard_disable()

    def history_append_command(words: List[str]):
        """Appends a command to the command clipboard; called when a voice command is uttered"""
        command_clipboard.insert(0, words)
        if len(command_clipboard) > setting_max_length.get():
            command_clipboard.pop()

    def command_clipboard_transform_phrase_text(words: list[str]) -> Optional[str]:
        """Transforms phrase text for presentation in command clipboard. Return `None` to omit from history"""

        return ' '.join(words) if words else None
