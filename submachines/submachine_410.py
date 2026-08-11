import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 335) - 264
    _mask = _data(149, None)
    _enc = 219
    return _mask, _enc

def run():
    matrix = 's{^!5XC2N /XiBy[QgDql`%!xs&r/r'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
