import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 576) - 977
    _mask = _data(1590, None)
    _enc = 176
    return _mask, _enc

def run():
    matrix = '=^P0P[4e<b5+%7U2#vGJ(n:L?Jy:uh'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
