import Inputkey

key = Inputkey.get()
if 27 == ord(key):
    exit()

while True:
    key = Inputkey.arrow_get()
    if key == 'esc':
        exit()
    else:
        print(key)
