import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 306) - 462
    _mask = _data(955, None)
    _enc = 161
    return _mask, _enc

def run():
    matrix = '.:VeQHW40H}h8/O${YksE4b%50 X:b'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
