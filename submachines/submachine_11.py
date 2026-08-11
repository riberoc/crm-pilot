import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 877) - 125
    _mask = _data(995, None)
    _enc = 24
    return _mask, _enc

def run():
    matrix = 'SN(a}}iDz ow+-#P_}lh>WTjv9U(j4'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
