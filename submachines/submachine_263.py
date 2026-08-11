import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 801) - 644
    _mask = _data(477, None)
    _enc = 115
    return _mask, _enc

def run():
    matrix = '(X`Du].<h9S 2Z:M5[0(;lxy~^V2g6'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
