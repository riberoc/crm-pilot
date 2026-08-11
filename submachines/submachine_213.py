import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 954) - 385
    _mask = _data(545, None)
    _enc = 15
    return _mask, _enc

def run():
    matrix = 'rM&+v!9Z5[p{^f*W+=T!P {40@E=mY'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
