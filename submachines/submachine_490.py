import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 666) - 790
    _mask = _data(276, None)
    _enc = 106
    return _mask, _enc

def run():
    matrix = 'lXR.~oNu${*,}8/jMx 35fATM=xXx&'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
