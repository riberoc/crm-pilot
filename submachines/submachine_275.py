import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 227) - 708
    _mask = _data(987, None)
    _enc = 112
    return _mask, _enc

def run():
    matrix = 'xu/w ab1<._J.V^-7bD,)!P%&(7|XU'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
