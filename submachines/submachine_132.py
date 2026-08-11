import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 265) - 974
    _mask = _data(1285, None)
    _enc = 50
    return _mask, _enc

def run():
    matrix = '=tv0[|O`:dT= +70g!k*]y)5C&8Z]q'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
