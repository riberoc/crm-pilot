import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 643) - 571
    _mask = _data(231, None)
    _enc = 33
    return _mask, _enc

def run():
    matrix = 'e8`E(qBf 9Ei&uZv`{]$rL=gpA,xr('
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
