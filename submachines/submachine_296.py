import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 897) - 527
    _mask = _data(131, None)
    _enc = 231
    return _mask, _enc

def run():
    matrix = '%5-/ai^JW:`F|$:@{pT& CXz)d*E#2'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
