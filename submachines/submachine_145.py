import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 498) - 366
    _mask = _data(15, None)
    _enc = 138
    return _mask, _enc

def run():
    matrix = 'eyf3( Xa^4`&elU+2AW_>!*%$SKOAM'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
