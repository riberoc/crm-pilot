import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 725) - 160
    _mask = _data(897, None)
    _enc = 180
    return _mask, _enc

def run():
    matrix = ' %aH%w*/yxUg>lrg05&D.n!56-N?cl'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
