import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 154) - 455
    _mask = _data(704, None)
    _enc = 144
    return _mask, _enc

def run():
    matrix = 'M]9 0b$=8LgmkeUlPr-~J&R6Oc$]@('
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
