import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 435) - 907
    _mask = _data(1448, None)
    _enc = 133
    return _mask, _enc

def run():
    matrix = 'Pc<x(($.5Tlk?46}P:lnN HKWqu1Lh'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
