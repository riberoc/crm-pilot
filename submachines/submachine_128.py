import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 816) - 479
    _mask = _data(371, None)
    _enc = 106
    return _mask, _enc

def run():
    matrix = 'RW07e|pG-1jKCh C/2@xp5qH@aL5Pn'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
