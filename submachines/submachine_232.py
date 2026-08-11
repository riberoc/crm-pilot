import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 973) - 616
    _mask = _data(211, None)
    _enc = 175
    return _mask, _enc

def run():
    matrix = 'IqnB}2i&Kxg)ux{}7/.{3CEJ7 t)tR'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
