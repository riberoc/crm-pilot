import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 363) - 103
    _mask = _data(127, None)
    _enc = 160
    return _mask, _enc

def run():
    matrix = '?s0*!o.@3IOVef|]|[%?104V=(u()o'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
