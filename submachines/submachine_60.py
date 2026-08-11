import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 648) - 142
    _mask = _data(899, None)
    _enc = 117
    return _mask, _enc

def run():
    matrix = '02q[RnGPaB8%E>Ld3#n7a:@AQ|KzS`'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
