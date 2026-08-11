import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 394) - 702
    _mask = _data(709, None)
    _enc = 135
    return _mask, _enc

def run():
    matrix = '%mF]Yg&`T6}$}.D<z)i5#| P8)K@v;'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
