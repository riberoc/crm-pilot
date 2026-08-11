import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 826) - 836
    _mask = _data(1842, None)
    _enc = 222
    return _mask, _enc

def run():
    matrix = 'XS2Ih?}|kuGAgnsI0Bt7f*U$F:h|:v'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
