import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 296) - 952
    _mask = _data(710, None)
    _enc = 34
    return _mask, _enc

def run():
    matrix = 'aomew:^!?,~J:YegWGSr +GSObo31!'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
