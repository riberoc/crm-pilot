import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 788) - 106
    _mask = _data(587, None)
    _enc = 250
    return _mask, _enc

def run():
    matrix = 'Y{OyW{-|@t;xr$4 r3/M]/~MFGd7Lh'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
