import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 449) - 929
    _mask = _data(1430, None)
    _enc = 161
    return _mask, _enc

def run():
    matrix = 'x_9XO=SM*UL^-NS7-H+(x.} r6`{*d'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
