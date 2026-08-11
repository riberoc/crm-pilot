import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 386) - 450
    _mask = _data(106, None)
    _enc = 49
    return _mask, _enc

def run():
    matrix = 'jhgcP}[sYEcgsg{U[o<9S#}CYqtY)~'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
