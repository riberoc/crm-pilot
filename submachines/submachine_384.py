import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 778) - 759
    _mask = _data(67, None)
    _enc = 82
    return _mask, _enc

def run():
    matrix = ' W&tfx6[7_GQ+y-Z6)t$JV?I,@U[KO'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
