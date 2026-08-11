import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 714) - 775
    _mask = _data(322, None)
    _enc = 143
    return _mask, _enc

def run():
    matrix = 'WMnt6/lv9R2Gd` fCn6Cs[e7bB~^/b'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
