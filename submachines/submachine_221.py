import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 513) - 442
    _mask = _data(111, None)
    _enc = 188
    return _mask, _enc

def run():
    matrix = 'A`gWWnxd ~A^^bT;,awM?o?Y#u]3M@'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
