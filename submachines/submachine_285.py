import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 861) - 219
    _mask = _data(946, None)
    _enc = 21
    return _mask, _enc

def run():
    matrix = 'jh|hUB$ML`#m?}ny}tKXRqXx{=J[kx'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
