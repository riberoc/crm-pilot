import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 722) - 286
    _mask = _data(887, None)
    _enc = 144
    return _mask, _enc

def run():
    matrix = 'cK!`|W__uG]8@,e09SvpKXk yFo9{C'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
