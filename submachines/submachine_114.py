import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 519) - 260
    _mask = _data(838, None)
    _enc = 53
    return _mask, _enc

def run():
    matrix = '/z0V:KjF /`V`y`?<8Hx!K(X(G>+$Q'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
