import PySimpleGUI as sg 

label = sg.Text('Enter feet: ')
input = sg.Input()

label_2 = sg.Text('Enter inches: ')
input_2 = sg.Input()

button = sg.Button('Convert')

window = sg.Window('Convertor', layout=[[label, input],
                                        [label_2, input_2],
                                        [button]])

window.read()
window.close()