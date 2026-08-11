import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 126) - 108
    _mask = _data(168, None)
    _enc = 125
    return _mask, _enc

def run():
    matrix = 'dexlZw84laGhZKyf2DXb$p2 EClcXn'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
