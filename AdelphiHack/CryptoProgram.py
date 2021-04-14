# Author: Omer Basar
# Filename: CryptoProgram.py
# Version: 4/14/21
# Additional Notes: Learned how to use PySimpleGUI from their website
# https://pysimplegui.readthedocs.io/en/latest/cookbook/#recipe-pattern-2b-persistent-window-multiple-reads-using-an-event-loop-updates-data-in-window
# Additional Notes: Learned how to use multiple layouts from the creator
# https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Column_Elem_Swap_Entire_Window.py

# ----------------------------------------------------------------
# Import GUI program and the cryptographic protocols
import PySimpleGUI as sg
import EncryptionProtocol as encryption
import DecryptionProtocol as decryption

# ----------------------------------------------------------------
# Implement the 3 layouts that we will be switching between

# Create the main menu layout
layout1 = [[sg.Text('Select one of the options from below.')],
           [sg.Button('Encryption'), sg.Button('Decryption'), sg.Button('Exit')]]

# Create the layout for the encryption program
layout2 = [[sg.Text('Enter a text to be encrypted.')],
           [sg.Text('Note: All non-alphabetical symbols will be ignored/stripped during processing.')],
           [sg.InputText()], [sg.Button('Enter'), sg.Button('Return')]]

# Create the layout ofr the decryption program
layout3 = [[sg.Text('Enter a cipher to be decrypted.')],
           [sg.InputText()], [sg.Button('Submit'), sg.Button("Go Back")]]

# ---------------------------------------------------------------
# Create actual layout using Columns, only showing the ones necessary at the moment
layout = [[sg.Column(layout1, key='-COL1-'), 
           sg.Column(layout2, visible=False, key='-COL2-'), 
           sg.Column(layout3, visible=False, key='-COL3-')]]

# Create the window which will display the layouts
window = sg.Window('Cryptography Module', layout)

# Assign layout to the integer representing the currently visible layout
layout = 1

#----------------------------------------------------------------
# Create a loop that keeps the window open until the user selects an exit condition
while True:
    # Reads all events and values that are present on the window
    event, values = window.read()
    
    # If user clicks the encryption button, performs the encryption protocol program
    if event == 'Encryption':

        # Enter loop that keeps the current layout/window open until quiting
        while True:

            # Hides the current visible layout and changes it to the encryption layout
            window[f'-COL{layout}-'].update(visible=False)
            layout = 2
            window[f'-COL{layout}-'].update(visible=True)

            # Reads all events and values that are present on the window
            event, values = window.read()
            
            # If user decides to quit this section, returns to main menu layout and breaks loop
            if event in (None, 'Return'):
                window[f'-COL{layout}-'].update(visible=False)
                layout = 1
                window[f'-COL{layout}-'].update(visible=True)
                break

            # If user decides to input a message to encrypt
            elif event == 'Enter':

                # Stores what the user types and converts to string if necessary
                textInput = str(values[0])

                # Processes user input by calling the encryption protocol
                textInput = encryption.characterEncoder(textInput)

                # If the user enters no input or only non-alphabetical symbols
                if (textInput == ""):
                    sg.popup_error("No Proper Input Detected:", "Please enter a message using only english alphabetical letters to encrypt.", title="Warning")
                
                # Displays the output if correct input was provided
                else:
                    sg.popup("Here is your encrypted message:", textInput, title="Encryption")
    
    # If user clicks the decryption button, performs the decryption protocol program
    elif event == 'Decryption':

        # Enter loop that keeps the current layout/window open until quiting
        while True:

            # Hides the current visible layout and changes it to the encryption layout
            window[f'-COL{layout}-'].update(visible=False)
            layout = 3
            window[f'-COL{layout}-'].update(visible=True)

            # Reads all events and values that are present on the window
            event, values = window.read()
            
            # If user decides to quit this section, returns to main menu layout and breaks loop
            if event in (None, 'Go Back'):
                window[f'-COL{layout}-'].update(visible=False)
                layout = 1
                window[f'-COL{layout}-'].update(visible=True)
                break

            # If user decides to input a message to encrypt
            elif event == 'Submit':

                # Stores what the user types and converts to string if necessary
                textInput = str(values[1])

                # Try block which attempts to decrypt the cipher.
                try:

                    # Processes user input by calling the encryption protocol
                    textInput= decryption.characterDecoder(textInput)

                    # Fail-safe which detects if no input is provided
                    if textInput == "":
                        sg.popup_error("No Input Detected:", "Please enter a hexadecimal cipher to decrypt.", title="Warning")
                    
                    # Displays the output if correct input was provided
                    else:
                        sg.popup("Here is your decrypted message:", textInput, title="Decryption")
                
                # Catches ValueError exception that pops up when user attempts to pass non-heaxadecimal strings
                except Exception: 
                    sg.popup_error("Incorrect Input:", "Make sure they are hexadecimals.", title="Warning")     

    # Once user hits the exit button to quit, breaks the loop
    elif event in (sg.WIN_CLOSED, 'Exit'):
        break

# Finally closes the window, ending the program
window.close()