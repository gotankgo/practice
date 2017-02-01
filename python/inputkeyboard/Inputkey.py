import sys, tty, termios, time

class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            # 방향키 읽으려면 3으로 줘야함
            # 이유: 방향키가 이스케이프문자포함해서 3자리
            # 그런데 3으로 주면 일반문자 3자리쌓여야 출력함
            ch = sys.stdin.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        return ch


def get():
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
            input_key = raw_key()
            if input_key != '':
                break

        if input_key in ARROW_KEY.keys():
            return ARROW_KEY.get(input_key)
        else:
            continue
        # esc키입력시 종료
        # if 27 == ord(input_key):
        #    exit()
        # 문자열 반환
        # return input_key

        
    