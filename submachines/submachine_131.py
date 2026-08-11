import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 663) - 206
    _mask = _data(971, None)
    _enc = 148
    return _mask, _enc

def run():
    matrix = 'GhSug;-ht?%T;;DW)z00Esw]R1 0LN'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
