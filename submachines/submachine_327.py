import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 244) - 490
    _mask = _data(756, None)
    _enc = 24
    return _mask, _enc

def run():
    matrix = '-@>BiYaQoc+<3NT}ecbo~Hc(5[)JT%'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
