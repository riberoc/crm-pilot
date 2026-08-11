import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 150) - 477
    _mask = _data(554, None)
    _enc = 202
    return _mask, _enc

def run():
    matrix = 'aFil/$C/T>+vG4.0%Z-ppF6#}{LeRN'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
