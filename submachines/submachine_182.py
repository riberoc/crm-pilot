import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 165) - 182
    _mask = _data(471, None)
    _enc = 181
    return _mask, _enc

def run():
    matrix = 'w73+(XIyW QE%}ixVD@kqB1QlwfR%1'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
