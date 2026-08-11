import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 420) - 276
    _mask = _data(136, None)
    _enc = 0
    return _mask, _enc

def run():
    matrix = 'js8E?R%9yBi2s6%j5n$xU:aCT$94VV'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
