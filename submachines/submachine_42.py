import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 991) - 515
    _mask = _data(316, None)
    _enc = 250
    return _mask, _enc

def run():
    matrix = 'evyo2L^]0R7[U!Uv`F>rITWYLr Q~l'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
