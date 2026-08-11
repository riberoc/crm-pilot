import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 362) - 282
    _mask = _data(872, None)
    _enc = 224
    return _mask, _enc

def run():
    matrix = 'F&;e(wV9ef60H<<Dk~z2.xbOn1W&Z)'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
