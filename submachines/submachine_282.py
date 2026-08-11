import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 394) - 807
    _mask = _data(633, None)
    _enc = 215
    return _mask, _enc

def run():
    matrix = 'Y1]<2C&YB&cseB:5jxv8]m`V!yE b&'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
