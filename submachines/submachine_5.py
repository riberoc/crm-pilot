import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 396) - 143
    _mask = _data(333, None)
    _enc = 52
    return _mask, _enc

def run():
    matrix = ';GY<%xm2aY8eU]G;X%n>vvw[M.!WMc'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
