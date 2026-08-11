import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 101) - 702
    _mask = _data(1018, None)
    _enc = 233
    return _mask, _enc

def run():
    matrix = '_IWDo%Vq bgB^dgZe,b9`Z{8mFoCf*'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
