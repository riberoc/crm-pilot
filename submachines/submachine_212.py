import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 587) - 846
    _mask = _data(414, None)
    _enc = 151
    return _mask, _enc

def run():
    matrix = 'Rlpua72)sDl.1X%O !P;^<JYbRpojd'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
