import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 801) - 283
    _mask = _data(629, None)
    _enc = 32
    return _mask, _enc

def run():
    matrix = '[l-1d#MXI{*V}jpZot2F1B4B} 5JeO'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
