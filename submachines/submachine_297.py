import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 838) - 396
    _mask = _data(750, None)
    _enc = 15
    return _mask, _enc

def run():
    matrix = 'Xo/QITvzT9I=:crp}5K Cc;u-M<Y>b'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
