import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 186) - 873
    _mask = _data(862, None)
    _enc = 104
    return _mask, _enc

def run():
    matrix = 'M4~$1!D}N_?FB6#G{ETepCyi{R*9Kn'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
