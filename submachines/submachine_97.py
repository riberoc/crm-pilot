import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 127) - 281
    _mask = _data(441, None)
    _enc = 189
    return _mask, _enc

def run():
    matrix = 'Q>Q9o?_T(=~EfDG_ v/G8vavsS[~PN'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
