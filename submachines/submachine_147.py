import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 432) - 812
    _mask = _data(519, None)
    _enc = 146
    return _mask, _enc

def run():
    matrix = '%L-i}<X`5R`/XD5{58;m+$w/g =<jj'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
