import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 813) - 346
    _mask = _data(277, None)
    _enc = 199
    return _mask, _enc

def run():
    matrix = 'R#cdDQ^xb&g,k|,9$IlQlmUo/ 1%A.'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
