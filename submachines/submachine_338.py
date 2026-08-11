import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 869) - 894
    _mask = _data(1837, None)
    _enc = 215
    return _mask, _enc

def run():
    matrix = 'Dy)rWZh,;E9CA}8b#g))L*nq}O}`E '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
