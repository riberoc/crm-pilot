import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 386) - 334
    _mask = _data(14, None)
    _enc = 48
    return _mask, _enc

def run():
    matrix = 'P[lM3.*Rn#@$fC tI6QdCN>*mHJKM!'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
