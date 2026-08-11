import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 463) - 593
    _mask = _data(945, None)
    _enc = 46
    return _mask, _enc

def run():
    matrix = "o%4'Gu^6!7jB{CN7`,fNBJMCB](/ZB"
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
