import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 571) - 271
    _mask = _data(787, None)
    _enc = 13
    return _mask, _enc

def run():
    matrix = 'vV88kszg+&Z(Al#SC5xt m=w?wXLSe'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
