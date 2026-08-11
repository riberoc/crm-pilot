import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 549) - 337
    _mask = _data(3, None)
    _enc = 208
    return _mask, _enc

def run():
    matrix = 'l1Q7j )Y@x`CPlmnjbkwU3-_65HJkE'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
