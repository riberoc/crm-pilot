import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 374) - 451
    _mask = _data(892, None)
    _enc = 84
    return _mask, _enc

def run():
    matrix = 'a!e{zR6e|O+wa4zDL,@ ;9#Dx9se*i'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
