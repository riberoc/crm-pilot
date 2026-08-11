import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 906) - 544
    _mask = _data(379, None)
    _enc = 217
    return _mask, _enc

def run():
    matrix = '5M#!0)Ijs>L(onsD<t&(wPy;}=-nC/'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
