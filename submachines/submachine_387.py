import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 226) - 151
    _mask = _data(414, None)
    _enc = 235
    return _mask, _enc

def run():
    matrix = 'BYeONL[=85Pal-aR=Yf34Oy;r6@e9p'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
