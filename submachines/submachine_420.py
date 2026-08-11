import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 903) - 351
    _mask = _data(394, None)
    _enc = 166
    return _mask, _enc

def run():
    matrix = '%-kH3]<O /+V*3/3rXL#3oGR4%@]_:'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
