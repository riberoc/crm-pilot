import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 310) - 290
    _mask = _data(136, None)
    _enc = 144
    return _mask, _enc

def run():
    matrix = 'Fkyl4WgJPwllm;5BX}j}Sz?(b2cL5#'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
