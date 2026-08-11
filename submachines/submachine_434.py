import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 558) - 295
    _mask = _data(881, None)
    _enc = 35
    return _mask, _enc

def run():
    matrix = 'zq$0;n@NN68Cu9BCZW|!aSdINy[HP2'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
