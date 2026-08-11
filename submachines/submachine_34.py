import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 475) - 746
    _mask = _data(627, None)
    _enc = 177
    return _mask, _enc

def run():
    matrix = '2O6rS_F[W#H:_Zo rY8@uDK]{@dZ(u'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
