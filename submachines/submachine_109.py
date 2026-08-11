import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 987) - 419
    _mask = _data(476, None)
    _enc = 109
    return _mask, _enc

def run():
    matrix = '|6kQqH1D, !y]T]Q0T]mVw|)~/;RK]'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
