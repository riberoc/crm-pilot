import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 654) - 593
    _mask = _data(397, None)
    _enc = 178
    return _mask, _enc

def run():
    matrix = 'efm+T-*T=-k<L}%e{,mYYTc5#n.!;!'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
