import PySimpleGUIWx as sg
import gspread


sg.theme('DarkBlack')    # Keep things interesting for your users

event, values = sg.Window('Login Window',
                  [[sg.Text(text="Enter the path to the google sheets registration file",font="Default 12")],[sg.In(key='-PathToLogin-')],
                  [sg.B('Enter')]],auto_size_text=True,auto_size_buttons=True)
GspreadLoginPath = values['-PathToLogin-']

if GspreadLoginPath == None:
    event.close()
print(f"Gspread Login Path - {GspreadLoginPath}")