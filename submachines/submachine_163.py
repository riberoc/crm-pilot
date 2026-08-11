import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 365) - 884
    _mask = _data(754, None)
    _enc = 35
    return _mask, _enc

def run():
    matrix = 'H#w8F5[: X|}eELNr=e0G_Xd4HGoPk'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
