import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 874) - 325
    _mask = _data(538, None)
    _enc = 36
    return _mask, _enc

def run():
    matrix = '3y3v8!wvJ&3&?Iz hA<|6?><FuTl43'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
