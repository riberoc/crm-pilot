import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 479) - 127
    _mask = _data(270, None)
    _enc = 92
    return _mask, _enc

def run():
    matrix = 'm(5SPINz|x`7?x h_!QrG-zf4c:-h@'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
