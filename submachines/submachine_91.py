import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 495) - 369
    _mask = _data(976, None)
    _enc = 221
    return _mask, _enc

def run():
    matrix = 'Sr8-|NOjx@IK/SSWJpD *B!nf$0%vH'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
