import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 267) - 690
    _mask = _data(672, None)
    _enc = 253
    return _mask, _enc

def run():
    matrix = 'F&~= ,0/NJRIX=VGX+-amb&;G[O&R#'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
