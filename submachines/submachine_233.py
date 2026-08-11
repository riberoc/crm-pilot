import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 205) - 109
    _mask = _data(508, None)
    _enc = 204
    return _mask, _enc

def run():
    matrix = 'nltmfD5A V;v3lmXyYL4rt@ibF:CoL'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
