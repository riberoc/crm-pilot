import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 596) - 511
    _mask = _data(243, None)
    _enc = 167
    return _mask, _enc

def run():
    matrix = '>B@C-2mqy|PR|OT qjt2S%0DkSZ6r?'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
