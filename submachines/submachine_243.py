import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 925) - 818
    _mask = _data(91, None)
    _enc = 143
    return _mask, _enc

def run():
    matrix = 'QIp1CRc_mep~eM3vnQ,i=kd?_~h wh'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
