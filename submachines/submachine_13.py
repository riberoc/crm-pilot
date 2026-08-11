import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 458) - 376
    _mask = _data(123, None)
    _enc = 35
    return _mask, _enc

def run():
    matrix = 'L4oT.5?AyNscp%a>lnYv(n(&/n 9Gn'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
