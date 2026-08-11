import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 408) - 632
    _mask = _data(768, None)
    _enc = 53
    return _mask, _enc

def run():
    matrix = 'T=|j{*#hdM{O4,]|.b5nh ndvWr!:2'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
