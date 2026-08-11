import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 996) - 642
    _mask = _data(213, None)
    _enc = 180
    return _mask, _enc

def run():
    matrix = 'Fip(V4q<SsGyA#;z59Yc8@WI:d/ s-'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
