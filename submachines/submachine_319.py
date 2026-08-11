import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 299) - 191
    _mask = _data(167, None)
    _enc = 193
    return _mask, _enc

def run():
    matrix = 'yosmdM#gh_7[ mYXF,J4H`qJ}23npx'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
