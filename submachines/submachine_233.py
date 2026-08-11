import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 241) - 788
    _mask = _data(878, None)
    _enc = 156
    return _mask, _enc

def run():
    matrix = 'V2Zp$k?!W.2==kWYAc,+fREa-awF18'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
