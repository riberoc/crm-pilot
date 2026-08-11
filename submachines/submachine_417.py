import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 810) - 225
    _mask = _data(515, None)
    _enc = 85
    return _mask, _enc

def run():
    matrix = '7>4OMlR*8cZMseH;&p]agjOK5/m)ft'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
