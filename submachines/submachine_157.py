import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 101) - 954
    _mask = _data(1144, None)
    _enc = 101
    return _mask, _enc

def run():
    matrix = '[?@uff ((^K2&89e*4>eh}u0k2]R6|'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
