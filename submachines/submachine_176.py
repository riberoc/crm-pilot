import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 385) - 422
    _mask = _data(994, None)
    _enc = 190
    return _mask, _enc

def run():
    matrix = '/IR TgIPi3U(if?U>~R7[E?.8<H:fW'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
