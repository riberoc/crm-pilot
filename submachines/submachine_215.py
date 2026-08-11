import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 759) - 660
    _mask = _data(53, None)
    _enc = 60
    return _mask, _enc

def run():
    matrix = 'lQ;~BSLM@UN~=FYfk$L5;F}+N0m;%!'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
