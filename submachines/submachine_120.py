import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 271) - 693
    _mask = _data(542, None)
    _enc = 68
    return _mask, _enc

def run():
    matrix = 'S-(mYjn:TZS)pe/J~Pm*(ZeD &VWO-'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
