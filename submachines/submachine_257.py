import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 963) - 606
    _mask = _data(353, None)
    _enc = 94
    return _mask, _enc

def run():
    matrix = 'XUqpMx%;nsXSHVg7>tI_Hr~oP+ 7ik'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
