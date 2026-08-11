import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 618) - 406
    _mask = _data(251, None)
    _enc = 227
    return _mask, _enc

def run():
    matrix = 'wcx4;)]4y!i9tao/%6e|Hb`6 <diIV'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
