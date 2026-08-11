import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 223) - 353
    _mask = _data(727, None)
    _enc = 177
    return _mask, _enc

def run():
    matrix = 'h`C-$k0>R?M`7r3YH{O{jPt)`r|w**'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
