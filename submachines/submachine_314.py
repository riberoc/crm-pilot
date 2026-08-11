import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 214) - 601
    _mask = _data(979, None)
    _enc = 182
    return _mask, _enc

def run():
    matrix = '=JcO+RL^dD-O`Ez,xn3S,apQ[c xrK'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
