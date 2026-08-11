import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 298) - 104
    _mask = _data(452, None)
    _enc = 129
    return _mask, _enc

def run():
    matrix = '$ALq:Cm pH7dcu)kMJ8X4gG1n&v(#I'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
