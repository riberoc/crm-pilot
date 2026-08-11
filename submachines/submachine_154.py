import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 957) - 993
    _mask = _data(1795, None)
    _enc = 192
    return _mask, _enc

def run():
    matrix = 'B#4~8IGcU0QUzTnZDwpgR=uwH}?Yd '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
