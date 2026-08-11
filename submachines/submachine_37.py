import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 387) - 247
    _mask = _data(215, None)
    _enc = 75
    return _mask, _enc

def run():
    matrix = 'ZC(YgS;h474}Xzg{>Dq]Ja X[XY(D<'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
