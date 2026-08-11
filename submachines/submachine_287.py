import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 138) - 547
    _mask = _data(910, None)
    _enc = 231
    return _mask, _enc

def run():
    matrix = 'wA6L.e [%+EL3_4J7=P]O^34gM/6K{'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
