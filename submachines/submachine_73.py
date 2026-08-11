import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 598) - 246
    _mask = _data(913, None)
    _enc = 220
    return _mask, _enc

def run():
    matrix = 'UB:+D/otaKb.w 31DD&+rQ<Hagy45i'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
