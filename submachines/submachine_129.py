import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 995) - 209
    _mask = _data(787, None)
    _enc = 27
    return _mask, _enc

def run():
    matrix = 'u8o5 _lIHw`6t)I+;O6)Z;/j6<zx*W'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
