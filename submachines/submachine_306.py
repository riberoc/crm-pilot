import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 764) - 168
    _mask = _data(1016, None)
    _enc = 80
    return _mask, _enc

def run():
    matrix = '3`{=dm{|ZaAF JJBq/(4f)@?t%D[|z'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
