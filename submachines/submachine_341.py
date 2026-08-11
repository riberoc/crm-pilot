import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 608) - 474
    _mask = _data(50, None)
    _enc = 107
    return _mask, _enc

def run():
    matrix = '5rJz9*odr>m5E=MUfCg u8^c9W^E*O'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
