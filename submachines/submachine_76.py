import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 402) - 322
    _mask = _data(231, None)
    _enc = 51
    return _mask, _enc

def run():
    matrix = ' e)[oXc-h$P#2O+T,X:3b0v^1qU*xZ'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
