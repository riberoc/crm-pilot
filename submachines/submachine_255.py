import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 186) - 638
    _mask = _data(597, None)
    _enc = 108
    return _mask, _enc

def run():
    matrix = '%3<.,;M{a[.UDpLTFv],RC2ju6Naq '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
