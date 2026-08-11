import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 349) - 585
    _mask = _data(613, None)
    _enc = 233
    return _mask, _enc

def run():
    matrix = '|S|(BT 18;we-]UE.gd1mCS>x14IUs'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
