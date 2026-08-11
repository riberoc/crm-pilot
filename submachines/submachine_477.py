import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 452) - 574
    _mask = _data(744, None)
    _enc = 243
    return _mask, _enc

def run():
    matrix = '!s#>}~uG.@bnz+AN;Np>tKnqZTuBwo'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
