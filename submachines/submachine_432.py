import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 409) - 937
    _mask = _data(633, None)
    _enc = 55
    return _mask, _enc

def run():
    matrix = ' A=Bz~RT<XYw3$&c+b~fwx2%9CTt^?'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
