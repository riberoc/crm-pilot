import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 424) - 819
    _mask = _data(715, None)
    _enc = 52
    return _mask, _enc

def run():
    matrix = '))?Uf/#[m2J`4p.<LObj|}a)T3153}'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
