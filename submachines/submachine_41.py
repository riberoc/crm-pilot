import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 515) - 339
    _mask = _data(984, None)
    _enc = 141
    return _mask, _enc

def run():
    matrix = 'RR(b, ;arY]JpO,&rh[o.)>*=n{mtl'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
