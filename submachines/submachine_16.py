import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 962) - 112
    _mask = _data(741, None)
    _enc = 162
    return _mask, _enc

def run():
    matrix = 'r+neEWRBu3NgQdlr#+@Fa %0*q)_4?'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
