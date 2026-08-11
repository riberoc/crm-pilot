import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 502) - 483
    _mask = _data(989, None)
    _enc = 66
    return _mask, _enc

def run():
    matrix = 'mRo1|y;c*r J{/5wgs3e#7HhlKur6k'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
