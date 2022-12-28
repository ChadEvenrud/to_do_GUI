import PySimpleGUI as sg 

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input(key='file')
choose_button1 = sg.FileBrowse("Choose")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input(key='location')
choose_button2 = sg.FolderBrowse("Choose")

window = sg.Window("File Compressor", layout=[[label1, input1, choose_button1], 
                                              [label2, input2, choose_button2]])


while True:
    event, values = window.read()
    print(event)
    print(values)
    
    match event:
       case sg.WIN_CLOSED:
            break

window.close()