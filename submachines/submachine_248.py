import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 584) - 711
    _mask = _data(508, None)
    _enc = 247
    return _mask, _enc

def run():
    matrix = '[o]5hmaA3[^.%//OvK2ld16A.Z 6W|'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
