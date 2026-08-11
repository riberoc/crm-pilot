import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 513) - 100
    _mask = _data(777, None)
    _enc = 165
    return _mask, _enc

def run():
    matrix = 't GnQ-Xt2aJXz~i,wpOdUOpyX<dmlO'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
