import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 505) - 669
    _mask = _data(694, None)
    _enc = 176
    return _mask, _enc

def run():
    matrix = 'b= p=g2GN{c6-rgkc;Gek/+|x_=4:-'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
