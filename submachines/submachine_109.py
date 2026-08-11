import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 252) - 567
    _mask = _data(675, None)
    _enc = 38
    return _mask, _enc

def run():
    matrix = 'qA3|AgkYmDv+2V 7_5|E6=e5|aB*Fo'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
