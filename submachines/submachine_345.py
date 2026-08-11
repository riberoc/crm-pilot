import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 764) - 925
    _mask = _data(1769, None)
    _enc = 107
    return _mask, _enc

def run():
    matrix = '<[{3$>-O)|0[RWq9O=s A#HT*Cur5<'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
