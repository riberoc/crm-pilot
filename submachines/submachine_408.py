import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 681) - 969
    _mask = _data(1642, None)
    _enc = 238
    return _mask, _enc

def run():
    matrix = 'eHoh`6g#D=O573]N1Bi+ ![)S~lf,N'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
