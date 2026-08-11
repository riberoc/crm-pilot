import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 363) - 982
    _mask = _data(1406, None)
    _enc = 41
    return _mask, _enc

def run():
    matrix = 's-m0+wn]}M-F]SAgyRGVT+ %,(<%PB'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
