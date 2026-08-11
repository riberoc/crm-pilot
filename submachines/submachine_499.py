import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 155) - 396
    _mask = _data(309, None)
    _enc = 44
    return _mask, _enc

def run():
    matrix = 'x1Ig)fXe;?HjZo ?kpt2h,=3>hS~,i'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
