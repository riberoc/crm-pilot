import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 653) - 148
    _mask = _data(618, None)
    _enc = 81
    return _mask, _enc

def run():
    matrix = 'SV BTn0}xT#Li?3f7.)vSvt7>3ozz#'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
