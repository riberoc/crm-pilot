import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 410) - 932
    _mask = _data(594, None)
    _enc = 57
    return _mask, _enc

def run():
    matrix = 'yhpBj1e730!DuYncY4~y82}f(Xoc4A'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
