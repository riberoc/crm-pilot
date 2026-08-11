import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 268) - 134
    _mask = _data(481, None)
    _enc = 110
    return _mask, _enc

def run():
    matrix = '`=xC/0<?itQ+q}3jNIi#uM<Kq`xpPI'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
