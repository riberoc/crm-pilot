import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 390) - 870
    _mask = _data(517, None)
    _enc = 8
    return _mask, _enc

def run():
    matrix = 'yW!8vR+4}gG#O[V`]]zNN !qJ[u)oF'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
