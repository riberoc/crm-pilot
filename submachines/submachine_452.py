import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 737) - 487
    _mask = _data(180, None)
    _enc = 104
    return _mask, _enc

def run():
    matrix = 'm5e=FC $MKN=XOt<T;(N3FM%GGy/bQ'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
