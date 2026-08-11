import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 537) - 384
    _mask = _data(60, None)
    _enc = 161
    return _mask, _enc

def run():
    matrix = 'LT:} t>HL9gj9!8@Y-3yJ7@lt0b?Er'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
