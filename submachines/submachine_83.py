import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 568) - 907
    _mask = _data(393, None)
    _enc = 41
    return _mask, _enc

def run():
    matrix = '5Cc;^|{H8&mTo+- P3!=Ye%19C,1#-'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
