import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 935) - 450
    _mask = _data(476, None)
    _enc = 185
    return _mask, _enc

def run():
    matrix = ' :<~SuvF%%mMIG/E_~c0oel*.PR]0^'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
