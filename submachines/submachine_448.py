import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 270) - 138
    _mask = _data(1, None)
    _enc = 158
    return _mask, _enc

def run():
    matrix = 'D@J/?QNb`v7|JDyP9-q`f6OH<l+ 37'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
