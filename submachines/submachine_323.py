import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 132) - 263
    _mask = _data(457, None)
    _enc = 86
    return _mask, _enc

def run():
    matrix = '!SnakVTdL.Fn}8kP s&Nz^sZ9GX=PZ'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
