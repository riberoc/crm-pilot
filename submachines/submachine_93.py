import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 291) - 149
    _mask = _data(61, None)
    _enc = 131
    return _mask, _enc

def run():
    matrix = 'kx6LG?u]LPsq&|n1lKTWs~0,e1Bs>u'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
