import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 504) - 896
    _mask = _data(603, None)
    _enc = 52
    return _mask, _enc

def run():
    matrix = 'Ae|kS~$W7tNKr}t=!Q%]-S< W0%ful'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
