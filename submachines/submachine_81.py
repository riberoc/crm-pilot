import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 218) - 253
    _mask = _data(487, None)
    _enc = 93
    return _mask, _enc

def run():
    matrix = '#S[#],R8o!/=u!bEjA2:/D,cDcamXs'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
