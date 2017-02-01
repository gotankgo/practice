import sys, tty, termios

class _Getch:
    def __call__(self, a):
        return self._get_key(a)

    def _get_key(self, a):
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(a)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        return ch

def get(a):
    ARROW_KEY = {
        '\x1b[A'        :'up',
        '\x1b[B'        :'down',
        '\x1b[C'        :'right',
        '\x1b[D'        :'left',
        '\x1b\x1b\x1b'  :'esc'
    }
    while True:
        raw_key = _Getch()
        while True:
            input_key = raw_key(a)
            if input_key != '':
                break

        if 3 == a:
            if input_key in ARROW_KEY.keys():
                return ARROW_KEY.get(input_key)
            else:
                continue
        elif 1 == a:
            return input_key
