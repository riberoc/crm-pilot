import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 234) - 265
    _mask = _data(323, None)
    _enc = 186
    return _mask, _enc

def run():
    matrix = 'S2ndN_;JaalwXW7<z`l}``SyI]uV}8'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
