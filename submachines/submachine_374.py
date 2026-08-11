import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 250) - 480
    _mask = _data(556, None)
    _enc = 230
    return _mask, _enc

def run():
    matrix = 'iV?gK68qjD3c_0KV YkTIS_O?xo!lR'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
