import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 144) - 112
    _mask = _data(402, None)
    _enc = 136
    return _mask, _enc

def run():
    matrix = ',G<GBVrtI3x;A<kd:.wW:or1`Sndf~'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
