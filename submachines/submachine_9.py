import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 667) - 370
    _mask = _data(818, None)
    _enc = 57
    return _mask, _enc

def run():
    matrix = 'ZR`DIUFhh57([t |F&n$8+YLw%OdxU'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
