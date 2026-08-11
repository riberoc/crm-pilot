import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 421) - 868
    _mask = _data(1464, None)
    _enc = 162
    return _mask, _enc

def run():
    matrix = 'Xg=a#2`-q|zE<uHZOuX>?.SV!E@ OK'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
