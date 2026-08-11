import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 592) - 257
    _mask = _data(899, None)
    _enc = 213
    return _mask, _enc

def run():
    matrix = '<.R=.lB bm>#9I`:b]W8&gR6U[,YF['
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
