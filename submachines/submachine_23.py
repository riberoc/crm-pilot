import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 587) - 681
    _mask = _data(382, None)
    _enc = 144
    return _mask, _enc

def run():
    matrix = '7.8cpgd|c)QOMUoJ8;L&-{&bh[~[ ]'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
