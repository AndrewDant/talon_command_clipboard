command clipboard: user.command_clipboard_toggle()
command clipboard close: user.command_clipboard_disable()
clip <number_small> (and <number_small>)*: user.command_clipboard_repeat_multi(number_small_list)
clip range <number_small> to <number_small>: user.command_clipboard_repeat_range(number_small_1, number_small_2)
clip (remove|chuck) <number_small> (and <number_small>)*: user.command_clipboard_trim_commands(number_small_list)

clip (show macro|macro show): user.command_clipboard_toggle_macro_gui()
(clip macro [play]|clip row): user.command_clipboard_play_macro()
clip macro add <number_small> (and <number_small>)*: user.command_clipboard_update_macro(number_small_list)
clip macro add <number_small> (through|past) <number_small>: user.command_clipboard_update_macro_range(number_small_1, number_small_2)
clip macro (remove|chuck) <number_small> (and <number_small>)*: user.command_clipboard_trim_macro(number_small_list)
clip macro clear all: user.command_clipboard_reset_macro()
clip macro copy [text]: user.command_clipboard_copy_macro()
clip macro update [text]: user.command_clipboard_save_macro()