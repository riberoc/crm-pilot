import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 285) - 557
    _mask = _data(964, None)
    _enc = 189
    return _mask, _enc

def run():
    matrix = 'e.X0y;}$_T};o)DF0 2ppfyY:DWLNy'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
