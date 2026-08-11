import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 424) - 216
    _mask = _data(324, None)
    _enc = 13
    return _mask, _enc

def run():
    matrix = ';qb[-FzVx$BGro&jUN$w5mAXt 5q46'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
