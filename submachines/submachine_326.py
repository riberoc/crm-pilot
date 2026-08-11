import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 876) - 420
    _mask = _data(656, None)
    _enc = 74
    return _mask, _enc

def run():
    matrix = 'SW+WaRzXHTAZokjs?M q>n4bGnSW(W'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
