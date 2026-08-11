import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 966) - 992
    _mask = _data(1975, None)
    _enc = 133
    return _mask, _enc

def run():
    matrix = '~4Pjw+mR~SRx$JzeJ}i. ,pu@I%8ti'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
