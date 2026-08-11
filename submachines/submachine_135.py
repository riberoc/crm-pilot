import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 523) - 351
    _mask = _data(947, None)
    _enc = 95
    return _mask, _enc

def run():
    matrix = 'Z@k|}^ ]d2tM6?322rd>z4ZdkBNOF#'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
