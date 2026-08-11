import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 492) - 969
    _mask = _data(1506, None)
    _enc = 73
    return _mask, _enc

def run():
    matrix = '`j#8QhM7{U?_ +UOyO2.~cL.mk>7wk'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
