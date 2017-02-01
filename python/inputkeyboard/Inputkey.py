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



def arrow_get():
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
            # 방향키 읽으려면 3으로 줘야함
            # 이유: 방향키가 이스케이프문자포함해서 3자리
            # 그런데 3으로 주면 일반문자 3자리쌓여야 출력함
            input_key = raw_key(3)
            if input_key != '':
                break

        if input_key in ARROW_KEY.keys():
            return ARROW_KEY.get(input_key)
        else:
            continue


def get():
    while True:
        raw_key = _Getch()        
        while True:
            input_key = raw_key(1)
            if input_key != '':
                break

        return input_key

        
    
