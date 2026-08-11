import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 681) - 141
    _mask = _data(933, None)
    _enc = 101
    return _mask, _enc

def run():
    matrix = '%cK_+RPC=Zk[?riMca.d;4_Zs[ Xfe'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
