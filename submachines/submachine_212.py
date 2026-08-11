import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 416) - 536
    _mask = _data(793, None)
    _enc = 181
    return _mask, _enc

def run():
    matrix = '/+`qCO1*Jd^q;alz4!^8u}nG;cXaG*'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
