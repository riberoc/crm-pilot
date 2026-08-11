import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 882) - 340
    _mask = _data(724, None)
    _enc = 68
    return _mask, _enc

def run():
    matrix = 'R`D98cPL{t?$.u3uApl)YU WQo+Sz('
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
