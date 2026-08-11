import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 892) - 377
    _mask = _data(735, None)
    _enc = 62
    return _mask, _enc

def run():
    matrix = '%,&wX;7}w;g[:-44gp,6 X%y@m*MD9'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
