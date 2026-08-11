import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 940) - 388
    _mask = _data(636, None)
    _enc = 67
    return _mask, _enc

def run():
    matrix = '94<,PkD>%-evd[Sez52F#lvHWHG@x~'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
