import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 340) - 409
    _mask = _data(797, None)
    _enc = 170
    return _mask, _enc

def run():
    matrix = 'Lyd[ES)^h-wN3!#N{:3tP:IF(d Bn('
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
