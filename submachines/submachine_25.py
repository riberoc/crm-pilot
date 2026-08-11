import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 850) - 213
    _mask = _data(737, None)
    _enc = 199
    return _mask, _enc

def run():
    matrix = 'gL6L#*0].uPf<L:h%[O.hE420 .ed{'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
