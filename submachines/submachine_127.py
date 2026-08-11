import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 103) - 737
    _mask = _data(810, None)
    _enc = 106
    return _mask, _enc

def run():
    matrix = 'vQ>)vw 9Z8JunAp?8KH_t;.`RBVepT'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
