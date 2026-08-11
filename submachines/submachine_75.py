import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 852) - 914
    _mask = _data(134, None)
    _enc = 77
    return _mask, _enc

def run():
    matrix = 'CEdPlQGxYEYFs .z5@1YPne@~|n/]2'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
