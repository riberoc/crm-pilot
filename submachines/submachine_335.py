import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 421) - 514
    _mask = _data(854, None)
    _enc = 250
    return _mask, _enc

def run():
    matrix = '4^MK7v}R?qP |).2$/{^>[Pg{>r~q/'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
