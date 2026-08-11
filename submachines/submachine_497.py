import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 706) - 130
    _mask = _data(939, None)
    _enc = 236
    return _mask, _enc

def run():
    matrix = '<7,T%AXTsN1 Kc>PRb~_ihLsPR[5o,'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
