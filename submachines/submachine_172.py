import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 413) - 441
    _mask = _data(994, None)
    _enc = 204
    return _mask, _enc

def run():
    matrix = ';Qjg0Oq4*Asfv=z<g83WMIxI(FgdF+'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
