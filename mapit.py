#!python3
#Launches a map webpage for whatever is entered in the command line
# or in the clipboard
import webbrowser, sys, pyperclip
print(10)
if len(sys.argv) > 1:
    #Stores a list of programs file name and arguments from the command line
    #sys.argv is a list of strings
    address = " ".join(sys.argv[1:])
    print((address))
else:
    #Get the address with clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)