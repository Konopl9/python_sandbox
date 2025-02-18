#!/Users/maksymmishchenko/Study/python_sandbox/.venv/bin/python
import webbrowser, sys, pyperclip

args = sys.argv
address = ""
if len(args) > 1:
    address = ' '.join(args[1:])
else:
    address = pyperclip.paste()
print(f"Address: {address}")  # Debug print
if address:
    webbrowser.open('https://www.google.com/maps/place/%s' % address)
    sys.exit()