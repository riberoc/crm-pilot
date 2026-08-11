import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 193) - 336
    _mask = _data(257, None)
    _enc = 123
    return _mask, _enc

def run():
    matrix = 'fJ26@0Xz6iU tn_(<V%[.t0d[Qa+G#'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
