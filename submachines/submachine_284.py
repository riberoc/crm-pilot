import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 893) - 977
    _mask = _data(135, None)
    _enc = 35
    return _mask, _enc

def run():
    matrix = 'n^tF@DfPRv wkcmm<7O%<6wXaIP&PP'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
