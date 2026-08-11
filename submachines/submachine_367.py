import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 243) - 227
    _mask = _data(360, None)
    _enc = 179
    return _mask, _enc

def run():
    matrix = 'aD$89+>O]V2 2I(At>IP7xIx1q:0*6'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
