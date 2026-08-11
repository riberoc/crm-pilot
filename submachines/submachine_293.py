import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 598) - 396
    _mask = _data(36, None)
    _enc = 251
    return _mask, _enc

def run():
    matrix = 'XM$[N$R^fAEL/<Lsx~)=y#=#U3$EQ '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
