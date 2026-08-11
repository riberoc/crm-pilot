import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 934) - 140
    _mask = _data(649, None)
    _enc = 168
    return _mask, _enc

def run():
    matrix = 'v^A?otQ;Ou.nGK[0M/LC01SUs@io$2'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
