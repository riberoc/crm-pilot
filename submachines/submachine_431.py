import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 486) - 253
    _mask = _data(123, None)
    _enc = 166
    return _mask, _enc

def run():
    matrix = 'tX1).# =2Z^O9eePE#FPgV;0+{7dr}'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
