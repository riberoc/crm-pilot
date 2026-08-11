import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 720) - 442
    _mask = _data(123, None)
    _enc = 228
    return _mask, _enc

def run():
    matrix = '?i>brt^/3NIO:0~OKoVO. FgS#k5bW'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
