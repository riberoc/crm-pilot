import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 775) - 109
    _mask = _data(539, None)
    _enc = 172
    return _mask, _enc

def run():
    matrix = '^n@ f>l$f*NaSVOB*0n-lXd/g*9*(P'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
