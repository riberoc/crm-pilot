import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 254) - 746
    _mask = _data(896, None)
    _enc = 132
    return _mask, _enc

def run():
    matrix = 'qBzhS-BiI|Dn3f3f m:1PHN~k6+Fb]'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
