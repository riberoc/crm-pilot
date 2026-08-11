import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 450) - 106
    _mask = _data(367, None)
    _enc = 65
    return _mask, _enc

def run():
    matrix = 'nPtn9<:Rb-7tNZ4=TDFuh5_A`d9^VF'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
