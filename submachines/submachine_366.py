import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 998) - 488
    _mask = _data(424, None)
    _enc = 106
    return _mask, _enc

def run():
    matrix = ':KLuZ[RqVCq7aUFYZlvR(dC,c51w8{'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
