import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 791) - 426
    _mask = _data(384, None)
    _enc = 244
    return _mask, _enc

def run():
    matrix = 'g_G>7Wv]%hJgEb*.n>2OX-n6(eE[!!'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
