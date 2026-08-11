import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 140) - 921
    _mask = _data(1270, None)
    _enc = 240
    return _mask, _enc

def run():
    matrix = 'GL1$_;Sj#__wCJ6KP_t,8W&Sk,S%Ui'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
