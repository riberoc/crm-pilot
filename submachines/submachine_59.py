import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 866) - 644
    _mask = _data(94, None)
    _enc = 189
    return _mask, _enc

def run():
    matrix = 'b/V4J CnDyEv;TuBV=6,8cR2`Oe-67'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
