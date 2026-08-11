import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 307) - 976
    _mask = _data(1358, None)
    _enc = 176
    return _mask, _enc

def run():
    matrix = 'r-4MT[:(*!zBz}R?vmf6.A`pI[uzO '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
