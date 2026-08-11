import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 266) - 493
    _mask = _data(854, None)
    _enc = 104
    return _mask, _enc

def run():
    matrix = '8wV?=a_ g(w~G_N:LQlN1~h{Pab[_@'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
