import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 380) - 236
    _mask = _data(153, None)
    _enc = 235
    return _mask, _enc

def run():
    matrix = '~gbc?b$u3!2439PBS- S5lw>,Nan($'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
