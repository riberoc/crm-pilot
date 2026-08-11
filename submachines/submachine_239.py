import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 975) - 900
    _mask = _data(57, None)
    _enc = 107
    return _mask, _enc

def run():
    matrix = 'ey;FmPd<l$ZcWxs5UcKqpUT)v z`tY'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
