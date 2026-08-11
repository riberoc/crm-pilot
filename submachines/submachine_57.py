import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 760) - 520
    _mask = _data(70, None)
    _enc = 182
    return _mask, _enc

def run():
    matrix = ' N/.ub_b5[5cUE{>DsS[AoRBjo}DqR'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
