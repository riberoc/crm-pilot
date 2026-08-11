import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 930) - 471
    _mask = _data(488, None)
    _enc = 127
    return _mask, _enc

def run():
    matrix = '-I{456Ho=UeI d!H.4~4)y%x~A?-#h'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
