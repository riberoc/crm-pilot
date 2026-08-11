import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 381) - 468
    _mask = _data(857, None)
    _enc = 89
    return _mask, _enc

def run():
    matrix = 'uW/p2sJp= ,ZRkI&e%0Jx3u$:e9}Sq'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
