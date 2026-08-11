import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 568) - 643
    _mask = _data(371, None)
    _enc = 217
    return _mask, _enc

def run():
    matrix = '2i=2Iw$j=}Qup8)^hca#K6ep]N(5vp'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
