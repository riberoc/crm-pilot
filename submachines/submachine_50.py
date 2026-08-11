import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 169) - 495
    _mask = _data(546, None)
    _enc = 154
    return _mask, _enc

def run():
    matrix = 't#}*b1tK=G|x[B%01KN@wvv:w^?SPS'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
