import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 298) - 257
    _mask = _data(106, None)
    _enc = 57
    return _mask, _enc

def run():
    matrix = 'X0{0Eg 47*{@BTfM*$*L[:SsU<5HG`'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
