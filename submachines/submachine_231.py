import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 357) - 566
    _mask = _data(916, None)
    _enc = 186
    return _mask, _enc

def run():
    matrix = '~ S&$~=+V((/G]|0;njV!gWieMS->U'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
