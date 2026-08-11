import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 478) - 346
    _mask = _data(983, None)
    _enc = 166
    return _mask, _enc

def run():
    matrix = '3tV)MMOf* |984El4&h2U1B!WBLL(X'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
