import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 581) - 590
    _mask = _data(144, None)
    _enc = 132
    return _mask, _enc

def run():
    matrix = '}u* +$-Sod9}&@OJ88;XO|R[$o)<@|'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
