import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 344) - 954
    _mask = _data(1304, None)
    _enc = 131
    return _mask, _enc

def run():
    matrix = 'GQa.R b?+^0S{,Ta5iLC`fI3lXnmMy'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
