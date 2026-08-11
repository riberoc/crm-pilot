import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 491) - 816
    _mask = _data(533, None)
    _enc = 200
    return _mask, _enc

def run():
    matrix = 'm1(k05 a#vX*6%SIF1dVd~GVwpBVR8'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
