import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 831) - 202
    _mask = _data(534, None)
    _enc = 89
    return _mask, _enc

def run():
    matrix = '<|,pgH gI:b;-oZMZ<4:W.lMN-s-*0'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
