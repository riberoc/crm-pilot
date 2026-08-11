import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 748) - 985
    _mask = _data(1675, None)
    _enc = 129
    return _mask, _enc

def run():
    matrix = '3uD9xr|{^80&?2x V?MOTc;,A4L]}3'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
