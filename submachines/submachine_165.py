import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 686) - 778
    _mask = _data(311, None)
    _enc = 134
    return _mask, _enc

def run():
    matrix = 'E7V|5Vy?< &g$N^WelM:;+UBGBg:HW'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
