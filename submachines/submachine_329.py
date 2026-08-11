import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 100) - 765
    _mask = _data(794, None)
    _enc = 137
    return _mask, _enc

def run():
    matrix = '}TAp9Vw~ xO`,MyE)?@q{s1vT6YEUQ'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
