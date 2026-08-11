import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 758) - 735
    _mask = _data(494, None)
    _enc = 53
    return _mask, _enc

def run():
    matrix = '=x.+?5FK/+*H UJ3.MOVqmS:P`YD7N'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
