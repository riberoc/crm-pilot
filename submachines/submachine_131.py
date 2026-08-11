import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 464) - 315
    _mask = _data(127, None)
    _enc = 104
    return _mask, _enc

def run():
    matrix = 'kE1am.}@(?5bHu_R!S[<1EF/RE8A i'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
