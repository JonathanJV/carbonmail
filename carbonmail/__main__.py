from carbonmail.email_sender import view

import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED


def enable_window():
    window  = view.get_window()

    while True:
        event, values=window.read()

        if event == WIN_CLOSED:
            window.close()
            break


enable_window() 