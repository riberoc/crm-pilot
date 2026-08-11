import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 213) - 323
    _mask = _data(349, None)
    _enc = 71
    return _mask, _enc

def run():
    matrix = 'h(_zLew!z9d!s{ycUm)]sC`98S[Cpy'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
