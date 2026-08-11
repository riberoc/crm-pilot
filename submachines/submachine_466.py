import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 105) - 778
    _mask = _data(957, None)
    _enc = 214
    return _mask, _enc

def run():
    matrix = 'L|CD9ZI?0LtMEQ5Pqnro~Xm@{j8ZnD'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
