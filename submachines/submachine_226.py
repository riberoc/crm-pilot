import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 576) - 505
    _mask = _data(175, None)
    _enc = 243
    return _mask, _enc

def run():
    matrix = '-,trF 1S5#-b4fD#tmu{NYw)8c=5%3'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
