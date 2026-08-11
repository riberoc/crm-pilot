import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 195) - 368
    _mask = _data(293, None)
    _enc = 125
    return _mask, _enc

def run():
    matrix = 'TgX76-Q7H+^ ^T(I$m`i:+M-_c2qI.'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
