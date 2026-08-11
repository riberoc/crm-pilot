import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 385) - 579
    _mask = _data(648, None)
    _enc = 214
    return _mask, _enc

def run():
    matrix = 'HxPaT8a&$f^7@3Vl cou2%W4|QgNjb'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
