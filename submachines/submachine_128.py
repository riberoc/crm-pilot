import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 892) - 291
    _mask = _data(731, None)
    _enc = 145
    return _mask, _enc

def run():
    matrix = 'S-5=#MU{L~6}:hRwnBjMo u6YIeXe}'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
