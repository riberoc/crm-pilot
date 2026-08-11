import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 709) - 349
    _mask = _data(792, None)
    _enc = 142
    return _mask, _enc

def run():
    matrix = 'U@#}$*7;fPK#f3 9]v&zD@1wh=[V@-'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
