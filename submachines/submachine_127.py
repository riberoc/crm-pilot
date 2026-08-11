import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 910) - 172
    _mask = _data(852, None)
    _enc = 41
    return _mask, _enc

def run():
    matrix = 'ZDW0:,o /VPsQ)yk<5z59/A^CUyw2>'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
