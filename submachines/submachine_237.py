import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 642) - 649
    _mask = _data(260, None)
    _enc = 228
    return _mask, _enc

def run():
    matrix = 'D(MQOJkzH/{:X%H6Em):PU3Eh ,g7,'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
