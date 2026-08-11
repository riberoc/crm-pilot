import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 467) - 719
    _mask = _data(828, None)
    _enc = 41
    return _mask, _enc

def run():
    matrix = 'mnSYA(yWY }c0>^SPN=e0(#.G>FOj^'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
