import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 357) - 718
    _mask = _data(747, None)
    _enc = 219
    return _mask, _enc

def run():
    matrix = 'Jp<w%Ae~kUQ}*~q`@JJ6b.e%va/ @;'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
