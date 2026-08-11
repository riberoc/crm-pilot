import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 279) - 308
    _mask = _data(191, None)
    _enc = 125
    return _mask, _enc

def run():
    matrix = 'LL#Q/o6u- g:Ad76>lE/8}s8Rh&j9#'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
