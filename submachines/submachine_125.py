import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 391) - 444
    _mask = _data(104, None)
    _enc = 50
    return _mask, _enc

def run():
    matrix = '+n6s;e;&{jT9?bTx$_1$~S]IB|;:0:'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
