import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 659) - 409
    _mask = _data(245, None)
    _enc = 208
    return _mask, _enc

def run():
    matrix = 'M}TT2e30$Jr#^8M#(.Y&Ss1j4:Y<p '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
