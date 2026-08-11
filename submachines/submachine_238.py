import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 895) - 471
    _mask = _data(505, None)
    _enc = 188
    return _mask, _enc

def run():
    matrix = '&hOS|D0C%!P=sZ)O!|6 $r*Jk/&<{5'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
