import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 893) - 761
    _mask = _data(163, None)
    _enc = 240
    return _mask, _enc

def run():
    matrix = 'hS)|DuMdAys`(3!5]8/%{a@>3P{Gl/'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
