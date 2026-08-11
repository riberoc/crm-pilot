import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 651) - 538
    _mask = _data(2, None)
    _enc = 123
    return _mask, _enc

def run():
    matrix = '#q*xFh(dJ4b{|:61YBiu VsonzU]qR'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
