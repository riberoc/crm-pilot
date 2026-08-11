import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 479) - 496
    _mask = _data(982, None)
    _enc = 11
    return _mask, _enc

def run():
    matrix = 'R/{*FUv^=#V&,QY1N7O&-aFG3F}XU_'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
