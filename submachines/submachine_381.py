import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 440) - 939
    _mask = _data(1419, None)
    _enc = 132
    return _mask, _enc

def run():
    matrix = '-kQ|Zv3v)8;u .m%p/Su(HJqN?0oOc'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
