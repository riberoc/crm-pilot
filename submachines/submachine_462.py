import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 990) - 409
    _mask = _data(537, None)
    _enc = 35
    return _mask, _enc

def run():
    matrix = '~e-&FHrZY,Axp ;(+$0$BF`)XF,Z}C'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
