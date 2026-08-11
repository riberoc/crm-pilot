import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 756) - 516
    _mask = _data(145, None)
    _enc = 116
    return _mask, _enc

def run():
    matrix = '3Q(bmDO=$=bRg->d^A{Z_ pBraJ/a/'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
