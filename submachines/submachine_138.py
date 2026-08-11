import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 874) - 535
    _mask = _data(508, None)
    _enc = 120
    return _mask, _enc

def run():
    matrix = '_rdkZs:df-HH)j6#9yd1_,@vlQ4D0]'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
