import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 655) - 633
    _mask = _data(474, None)
    _enc = 203
    return _mask, _enc

def run():
    matrix = 'RR%XPTT!IL+R(|C%Y;Q;-hu Icn1hz'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
