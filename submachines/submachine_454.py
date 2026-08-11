import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 432) - 951
    _mask = _data(1421, None)
    _enc = 159
    return _mask, _enc

def run():
    matrix = 'lr0(N$fTi;]~a5_+/6djnIIoP -vc#'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
