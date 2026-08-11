import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 175) - 524
    _mask = _data(537, None)
    _enc = 168
    return _mask, _enc

def run():
    matrix = '}- 1[.dc>7}TPP-E?E;zoXo%=eH=$Z'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
