import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 296) - 641
    _mask = _data(632, None)
    _enc = 194
    return _mask, _enc

def run():
    matrix = 'z2DWAP*z5foQHTH%=El7u%2Yl3gZ/B'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
