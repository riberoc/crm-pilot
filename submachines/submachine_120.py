import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 962) - 384
    _mask = _data(452, None)
    _enc = 135
    return _mask, _enc

def run():
    matrix = '~ m3IBLqoD$cY~^G5BEL+BJmEN2eRp'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
