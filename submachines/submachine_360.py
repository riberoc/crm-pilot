import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 634) - 270
    _mask = _data(1016, None)
    _enc = 109
    return _mask, _enc

def run():
    matrix = 'l2qSI=u{K^_!NMk@Qr]Z5P3Cn o)zo'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
