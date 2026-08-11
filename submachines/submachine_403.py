import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 950) - 913
    _mask = _data(1932, None)
    _enc = 168
    return _mask, _enc

def run():
    matrix = 'O uL_L>*f6beiNQ~`I]|-Jbv-j48Sp'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
