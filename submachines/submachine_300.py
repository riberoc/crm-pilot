import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 983) - 562
    _mask = _data(231, None)
    _enc = 254
    return _mask, _enc

def run():
    matrix = ' dW1B>+`yo1aJ(3R]=/=n<tVU0{}G%'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
