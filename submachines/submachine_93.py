import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 590) - 516
    _mask = _data(84, None)
    _enc = 19
    return _mask, _enc

def run():
    matrix = 'Tqw}e ),^vm8V@L/toy1v._+a&$V[m'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
