import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 479) - 825
    _mask = _data(1475, None)
    _enc = 241
    return _mask, _enc

def run():
    matrix = 'cyrZTv0Gy9mxN8(aVo TI%)sMT/T$I'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
