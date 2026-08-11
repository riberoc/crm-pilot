import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 984) - 260
    _mask = _data(601, None)
    _enc = 125
    return _mask, _enc

def run():
    matrix = ' @n1!fGdhK`BcG3DdIoO|yDij`}JQr'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
