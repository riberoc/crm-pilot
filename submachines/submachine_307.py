import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 883) - 591
    _mask = _data(499, None)
    _enc = 42
    return _mask, _enc

def run():
    matrix = 'Q0g3JWzfTVe!~si|yoQ!QFsdma+ f<'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
