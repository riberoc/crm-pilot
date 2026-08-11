import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 913) - 986
    _mask = _data(1858, None)
    _enc = 238
    return _mask, _enc

def run():
    matrix = 'oD+Y[ZQU*P6RwH%D?rp1?x^ _oZ1-7'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
