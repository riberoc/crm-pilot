import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 742) - 156
    _mask = _data(1014, None)
    _enc = 105
    return _mask, _enc

def run():
    matrix = '!:ZI$Uh*V-#ZBb/s[.Ood<f)3sG,} '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
