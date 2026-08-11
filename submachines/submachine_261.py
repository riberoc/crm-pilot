import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 102) - 783
    _mask = _data(812, None)
    _enc = 57
    return _mask, _enc

def run():
    matrix = 'q(a)SfcM|>BP`px^.D,aMxX%H+eb|%'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
