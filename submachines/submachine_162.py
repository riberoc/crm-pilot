import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 570) - 996
    _mask = _data(1585, None)
    _enc = 60
    return _mask, _enc

def run():
    matrix = ')EY=n|7l^2-RP1LYWmV(SNKU{7$ XF'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
