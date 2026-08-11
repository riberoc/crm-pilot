import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 835) - 144
    _mask = _data(1015, None)
    _enc = 48
    return _mask, _enc

def run():
    matrix = '1$T9$hF1ffs*4>J9qv_4 90k~k&9G['
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
