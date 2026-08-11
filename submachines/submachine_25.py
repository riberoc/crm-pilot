import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 277) - 320
    _mask = _data(149, None)
    _enc = 72
    return _mask, _enc

def run():
    matrix = '%X:SjeH$ z#fEDGXJ1Nr94(f+{VyAy'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
