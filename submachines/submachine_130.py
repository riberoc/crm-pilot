import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 577) - 920
    _mask = _data(1741, None)
    _enc = 247
    return _mask, _enc

def run():
    matrix = '}-B ^xPdKKe0{.?Hxl)B)An`dQb,7/'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
