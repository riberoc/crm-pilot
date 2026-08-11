import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 222) - 264
    _mask = _data(411, None)
    _enc = 40
    return _mask, _enc

def run():
    matrix = 'vy(KLiD+?1U3(XTTruAK{ ,~HwWGA^'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
