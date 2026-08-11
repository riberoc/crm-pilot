import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 649) - 760
    _mask = _data(458, None)
    _enc = 66
    return _mask, _enc

def run():
    matrix = '+<>{4$fp0 pH20Dd(JgBt5L#@:f=}2'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
