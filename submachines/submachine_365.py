import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 596) - 454
    _mask = _data(910, None)
    _enc = 6
    return _mask, _enc

def run():
    matrix = 'DM^K*3UGU+yP$HT;aF !eF]ADRP~|='
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
