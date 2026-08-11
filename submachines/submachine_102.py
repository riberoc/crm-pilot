import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 389) - 155
    _mask = _data(135, None)
    _enc = 111
    return _mask, _enc

def run():
    matrix = '=k+*,z8o &jY`&ogGURK/satcp61bl'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
