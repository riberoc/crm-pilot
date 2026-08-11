import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 248) - 924
    _mask = _data(1214, None)
    _enc = 165
    return _mask, _enc

def run():
    matrix = 'h>1`4dEsn_zww|Zeo|^uEHD48vVeEz'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
