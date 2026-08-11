import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 795) - 434
    _mask = _data(266, None)
    _enc = 83
    return _mask, _enc

def run():
    matrix = '6DveBMh0)]W> wUws1)W-WVFr,-$)e'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
