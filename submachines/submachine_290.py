import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 263) - 108
    _mask = _data(11, None)
    _enc = 160
    return _mask, _enc

def run():
    matrix = ' ]yUFhMJrr)d(aY;Q:Kisu^rY*NT5I'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
