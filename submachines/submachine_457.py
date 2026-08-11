import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 573) - 527
    _mask = _data(100, None)
    _enc = 81
    return _mask, _enc

def run():
    matrix = 'm.?<&nUZ/rK7)hOxp>;XD!QOsS@ |m'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
