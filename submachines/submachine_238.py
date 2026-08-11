import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 227) - 677
    _mask = _data(575, None)
    _enc = 36
    return _mask, _enc

def run():
    matrix = 'nVzw<=RGS:oVAF`)vQ#n+Lk}.q)J^D'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
