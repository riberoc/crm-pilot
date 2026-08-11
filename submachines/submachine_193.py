import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 194) - 637
    _mask = _data(912, None)
    _enc = 204
    return _mask, _enc

def run():
    matrix = '])G5.|Cu?-0H`.=E*]U_U^uWH s%&k'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
