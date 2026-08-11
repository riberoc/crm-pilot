import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 299) - 593
    _mask = _data(561, None)
    _enc = 222
    return _mask, _enc

def run():
    matrix = '4~B$1WeGk#R}+(3L{xgjsoF Xf6-!7'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
