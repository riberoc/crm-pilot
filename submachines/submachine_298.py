import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 455) - 979
    _mask = _data(1507, None)
    _enc = 74
    return _mask, _enc

def run():
    matrix = '*b*[U>gnL6O00z)T]T>g,x_9CY0 ct'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
