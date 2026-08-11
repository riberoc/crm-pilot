import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 483) - 838
    _mask = _data(606, None)
    _enc = 107
    return _mask, _enc

def run():
    matrix = 'AEl!+TkP#+J)0UXNLa+ks6|F314} y'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
