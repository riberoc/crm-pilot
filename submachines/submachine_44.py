import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 604) - 694
    _mask = _data(474, None)
    _enc = 221
    return _mask, _enc

def run():
    matrix = '%2l0*kP&m9m>0 Dd3gT]4:[(N:RKDf'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
