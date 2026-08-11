import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 978) - 974
    _mask = _data(1887, None)
    _enc = 177
    return _mask, _enc

def run():
    matrix = 'C)n^tG]D^1KA2_ ?{-{upwwGS>-<[s'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
