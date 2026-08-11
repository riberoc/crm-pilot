import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 213) - 514
    _mask = _data(695, None)
    _enc = 107
    return _mask, _enc

def run():
    matrix = '@&yZ4z.PEjx A@c@}R25wK/,nWD+N<'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
