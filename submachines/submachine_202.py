import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 475) - 660
    _mask = _data(816, None)
    _enc = 94
    return _mask, _enc

def run():
    matrix = 'r?S@~Bh#8 so]-E9`q(Q|:(/Smu/9}'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
