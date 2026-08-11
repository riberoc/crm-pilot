import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 879) - 869
    _mask = _data(255, None)
    _enc = 34
    return _mask, _enc

def run():
    matrix = '#:t{Oc;(H WM41k%7)J`$|2d?`d`VA'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
