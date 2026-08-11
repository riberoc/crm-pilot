import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 607) - 664
    _mask = _data(231, None)
    _enc = 46
    return _mask, _enc

def run():
    matrix = 's<$_1.&<suZsE`h^0izPE<)WJVMGKx'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
