import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 302) - 628
    _mask = _data(579, None)
    _enc = 255
    return _mask, _enc

def run():
    matrix = 'na4<24 `VW)X:W7O<)AZfyQ04o7x`]'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
