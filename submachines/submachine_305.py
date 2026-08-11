import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 195) - 550
    _mask = _data(553, None)
    _enc = 207
    return _mask, _enc

def run():
    matrix = 'P7S,er=D(G1 Hr>=yuKj}DuD`.aw#^'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
