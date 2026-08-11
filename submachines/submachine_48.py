import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 467) - 909
    _mask = _data(1425, None)
    _enc = 184
    return _mask, _enc

def run():
    matrix = '/m8w%WAvCUN:G $4v=<dGWroB%dDp%'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
