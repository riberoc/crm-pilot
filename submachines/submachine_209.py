import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 603) - 822
    _mask = _data(1602, None)
    _enc = 255
    return _mask, _enc

def run():
    matrix = 'Y&F?fLY/zrLbR7C=l>~gkCQaDNKC 5'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
