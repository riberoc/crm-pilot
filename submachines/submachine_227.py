import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 739) - 767
    _mask = _data(354, None)
    _enc = 137
    return _mask, _enc

def run():
    matrix = 'Y]4xI)niXIP NW$lrOZ#P:yi8m|h#/'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
