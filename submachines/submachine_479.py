import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 868) - 498
    _mask = _data(424, None)
    _enc = 217
    return _mask, _enc

def run():
    matrix = 'ZB: cn,![Fe=]019Eum1j_ITvk~mE3'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
