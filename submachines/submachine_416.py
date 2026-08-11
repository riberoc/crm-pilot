import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 311) - 786
    _mask = _data(577, None)
    _enc = 115
    return _mask, _enc

def run():
    matrix = 'o~#?z`%pvX_DyDZSo0J$K9$tml<gPb'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
