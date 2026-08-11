import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 204) - 730
    _mask = _data(1017, None)
    _enc = 83
    return _mask, _enc

def run():
    matrix = 'Y=UCyumO ua[ePB9DM?Ya.[J`9sgR)'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
