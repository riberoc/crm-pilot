import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 463) - 955
    _mask = _data(1427, None)
    _enc = 185
    return _mask, _enc

def run():
    matrix = '|?}65K!vby/J,ptwuo:k4iP* !nA3A'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
