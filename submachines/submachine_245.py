import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 617) - 642
    _mask = _data(167, None)
    _enc = 92
    return _mask, _enc

def run():
    matrix = '4`X2e`_@3^_wbn@1 x!wt1;u*_IE|)'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
