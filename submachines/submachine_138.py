import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 730) - 331
    _mask = _data(941, None)
    _enc = 34
    return _mask, _enc

def run():
    matrix = 'Q3ktm>rTvszO2e V9st!d(tsa%79U$'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
