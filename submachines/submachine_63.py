import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 750) - 721
    _mask = _data(3, None)
    _enc = 21
    return _mask, _enc

def run():
    matrix = '_hZipD4!qti>S/7`Do6fg).A}7tl75'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
