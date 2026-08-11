import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 256) - 436
    _mask = _data(768, None)
    _enc = 92
    return _mask, _enc

def run():
    matrix = '[=q}h~~-,)lHi_sP m{=qU0LJ)NYkC'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
