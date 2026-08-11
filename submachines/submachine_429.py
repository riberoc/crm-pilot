import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 117) - 992
    _mask = _data(1279, None)
    _enc = 186
    return _mask, _enc

def run():
    matrix = 'p<^br/P?4P.[Kfuk `l}?_,IE!`L(>'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
