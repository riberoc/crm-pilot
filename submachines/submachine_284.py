import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 352) - 153
    _mask = _data(13, None)
    _enc = 214
    return _mask, _enc

def run():
    matrix = '@rrwBY7W.[yDCeKLur1m|ls,+jpcpA'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
