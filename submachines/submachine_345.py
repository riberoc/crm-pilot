import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 156) - 963
    _mask = _data(876, None)
    _enc = 45
    return _mask, _enc

def run():
    matrix = 'hk+m:GZ3c`DbWH0+L!A|IDF^f]l9Vq'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
