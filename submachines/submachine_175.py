import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 147) - 537
    _mask = _data(732, None)
    _enc = 42
    return _mask, _enc

def run():
    matrix = '}*#3Qdc#7L@QmLR^.!S:<=x//KvZ 3'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
