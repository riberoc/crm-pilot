import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 567) - 189
    _mask = _data(721, None)
    _enc = 43
    return _mask, _enc

def run():
    matrix = '$^ MG-|>Cyv3Zi%^?VB{!v72z5w@as'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
