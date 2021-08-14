import PySimpleGUI as sg
from utils import *
sg.theme('BluePurple')

layout = [[sg.Text('Generated Password:'), sg.Text(size=(15, 1), key='-OUTPUT-')],
          [sg.Button('Generate')],
          [sg.Text('Website', size=(8, 1)), sg.InputText(key='-IN-')],
          [sg.Text('Password', size=(8, 1)), sg.InputText(key='-IN-2')],
          [sg.Text('Key', size=(8, 1)), sg.InputText(key='KEY')],
          [sg.Button("Store"), sg.Button("Encrypt"), sg.Button("Decrypt")],
          [sg.Button('Exit')]]

window = sg.Window('Password Generator', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        # Exit the program
        break
    if event == 'Generate':
        # Show the generated Password
        window['-OUTPUT-'].update(password_generator())
    if event ==  'Store':
        # Store website and password in My Data file
        if not values['-IN-'] or not values['-IN-2']:
            sg.popup_error('Empty values for website and password, please fill in!', title="Empty Data")
        else:
            website = values['-IN-'] 
            password = values['-IN-2']
            show_data_stored = store_login_data(website, password) + " stored"
            sg.popup(show_data_stored, title='Store Complete')
    if event == 'Encrypt':
        # Generate key and encrypt My Data file
        if file_encrypt(MY_DATA_FILE) is False:
            sg.popup('Your data is already encrypted, use decryption if you want to see your data',
            title="Data already encrypted")
    if event == 'Decrypt':
        # Decrypt My Data using the key created previously at encryption
        # Store this key very carefully!
        key_value = values['KEY']
        print(values['KEY'])
        if file_decrypt(MY_DATA_FILE, key_value) is False:
            sg.popup_error('Key is empty, fill in your key!', title="Decypt error")
window.close()