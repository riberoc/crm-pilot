import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 297) - 264
    _mask = _data(112, None)
    _enc = 73
    return _mask, _enc

def run():
    matrix = '`=7{.Ys%}&)$}-3-J@[Smng; I0/-1'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
