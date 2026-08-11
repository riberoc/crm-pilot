import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 536) - 172
    _mask = _data(839, None)
    _enc = 168
    return _mask, _enc

def run():
    matrix = '*KftlA}M*zZEHvf=zLl3:vL4L?4 ;S'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
