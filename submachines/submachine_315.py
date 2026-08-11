import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 895) - 401
    _mask = _data(366, None)
    _enc = 146
    return _mask, _enc

def run():
    matrix = 'F}$^_jYW#)0u{,hqY0 oen6:g&3q@k'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
