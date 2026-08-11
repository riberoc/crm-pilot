import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 487) - 387
    _mask = _data(21, None)
    _enc = 121
    return _mask, _enc

def run():
    matrix = 'gaX$>bksi(~G!s>ZPXb~:q yt:{^$C'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
