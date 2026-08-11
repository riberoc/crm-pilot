import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 196) - 510
    _mask = _data(539, None)
    _enc = 239
    return _mask, _enc

def run():
    matrix = 'wE~T}*w-oo;K0adtiu/3?RI8Z{]7V&'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
