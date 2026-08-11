import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 321) - 247
    _mask = _data(237, None)
    _enc = 173
    return _mask, _enc

def run():
    matrix = '8oML!]uN&*p+Q#ix`P?)%g|9 bI^<Q'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
