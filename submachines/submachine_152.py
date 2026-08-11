import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 567) - 810
    _mask = _data(447, None)
    _enc = 73
    return _mask, _enc

def run():
    matrix = 'e#+y9F;y9$^(ktnSp2lDa){ !JW6!s'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
