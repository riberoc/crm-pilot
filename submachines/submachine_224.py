import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 906) - 199
    _mask = _data(572, None)
    _enc = 227
    return _mask, _enc

def run():
    matrix = 'cC0d{>7g=F.)T.(F)PHI*:)[:c]H^Y'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
