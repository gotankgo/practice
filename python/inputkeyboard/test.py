import Inputkey

ARROW = 3
NOMAL = 1

key = Inputkey.get(NOMAL)
if 27 == ord(key):
    exit()

while True:
    key = Inputkey.get(ARROW)
    if key == 'esc':
        exit()
    else:
        print(key)
