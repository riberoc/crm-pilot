import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 967) - 532
    _mask = _data(203, None)
    _enc = 238
    return _mask, _enc

def run():
    matrix = '^`O@+xKZ(DgX`qCw=j(Q;pr~T@xd$d'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
