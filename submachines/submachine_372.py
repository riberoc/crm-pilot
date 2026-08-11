import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 228) - 266
    _mask = _data(386, None)
    _enc = 88
    return _mask, _enc

def run():
    matrix = '.1y- 3qa{P`XExMfMNJGQT-P6o&7@q'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
