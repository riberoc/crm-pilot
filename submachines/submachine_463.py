import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 408) - 998
    _mask = _data(1475, None)
    _enc = 108
    return _mask, _enc

def run():
    matrix = '/tig,/i/mLr!>jmY1F]#O*U}] (+(F'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
