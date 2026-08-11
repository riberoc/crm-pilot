import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 467) - 874
    _mask = _data(1504, None)
    _enc = 201
    return _mask, _enc

def run():
    matrix = 's^5Ki8z16&Wc:[c4`+s!Z2wS--jV;='
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
