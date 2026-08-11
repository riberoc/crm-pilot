import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 204) - 565
    _mask = _data(985, None)
    _enc = 237
    return _mask, _enc

def run():
    matrix = '.WRoe1``OrO@] #@NkPhUbbM7B8+IT'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
