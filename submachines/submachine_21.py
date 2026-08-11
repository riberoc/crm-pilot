import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 826) - 510
    _mask = _data(422, None)
    _enc = 135
    return _mask, _enc

def run():
    matrix = 'yfwvFUgcqGlBcXovG[$K,[S&m L<.r'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
