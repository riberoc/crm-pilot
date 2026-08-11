import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 819) - 998
    _mask = _data(1801, None)
    _enc = 71
    return _mask, _enc

def run():
    matrix = 'Hr<T2d8-A=t[O1Vl4{& e4pe/7qbLu'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
