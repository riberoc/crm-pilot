import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 850) - 139
    _mask = _data(601, None)
    _enc = 143
    return _mask, _enc

def run():
    matrix = '*pzoYZ^W&Q-AF<! k+mb~`hj#$_2Dz'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
