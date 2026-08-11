import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 845) - 586
    _mask = _data(290, None)
    _enc = 34
    return _mask, _enc

def run():
    matrix = '2%OAc<e rUH>3PJ2vFe%IEJ:fzB|eg'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
