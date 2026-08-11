import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 422) - 386
    _mask = _data(122, None)
    _enc = 87
    return _mask, _enc

def run():
    matrix = '@[;@kbNg$.akT *9rXnsgJpCN}1+oS'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
