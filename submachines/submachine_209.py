import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 815) - 473
    _mask = _data(305, None)
    _enc = 94
    return _mask, _enc

def run():
    matrix = '|Sn--[7gVYet{ssc=}<>rw#L{K+ e2'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
