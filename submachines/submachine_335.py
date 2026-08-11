import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 855) - 692
    _mask = _data(59, None)
    _enc = 188
    return _mask, _enc

def run():
    matrix = '-DB(r<H5z<d{BC_.H4=(UQd.BkL59b'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
