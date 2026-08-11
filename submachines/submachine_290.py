import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 624) - 764
    _mask = _data(401, None)
    _enc = 235
    return _mask, _enc

def run():
    matrix = '8v9oH`V?Mf8<)Hr(uP1=aDm__<~LOm'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
