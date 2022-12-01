import PySimpleGUI as sg
import gspread
import os.path
from time import sleep
sg.theme("GrayGrayGray")
ErrorWindow = False

window = sg.Window('Remote Cry Controller:Get Login File', [
                              [sg.Text('Input Filename of Login File')],
                              [sg.Input(key="-PathToLogin-"), sg.FileBrowse()],
                              [sg.OK(), sg.Cancel()]
                              ],icon="VirusIcon.ico")

while True:
    sleep(0.01)
    event, values = window.read()
    GspreadLoginPath = values['-PathToLogin-']

    try:
        if event == "OK":
            if os.path.exists(GspreadLoginPath):
                print(f"LoginPath{GspreadLoginPath}")
                window.close()
                break
            else:
                sg.popup_error("**** Invalid Filename ****",font="Default 13")
        elif event != "Cancel":
            window.close()
    except:
        pass
