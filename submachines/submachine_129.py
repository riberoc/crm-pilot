import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 454) - 898
    _mask = _data(1505, None)
    _enc = 172
    return _mask, _enc

def run():
    matrix = 'F.7=J$AEz *O7a^%zwlS8`w40AYt[?'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
