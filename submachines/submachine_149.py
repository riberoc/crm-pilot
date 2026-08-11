import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 867) - 219
    _mask = _data(759, None)
    _enc = 190
    return _mask, _enc

def run():
    matrix = '=bp+[Zt kxYC9djO@v]/]^1w5yxj(m'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
