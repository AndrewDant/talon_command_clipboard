command clipboard: user.command_clipboard_toggle()
command clipboard close: user.command_clipboard_disable()
clip <user.clip_set>: user.command_clipboard_repeat_multi(clip_set)
clip range <number_small> to <number_small>: user.command_clipboard_repeat_range(number_small_1, number_small_2)

show [clip] macro: user.command_clipboard_toggle_macro_gui()
clip macro [play]: user.command_clipboard_play_macro()
clip macro add <user.clip_set>: user.command_clipboard_update_macro(clip_set)
clip macro remove <number_small> (and <number_small>)*: user.command_clipboard_trim_macro(number_small_list)
clip macro remove all: user.command_clipboard_reset_macro()
