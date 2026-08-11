import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 938) - 928
    _mask = _data(1944, None)
    _enc = 157
    return _mask, _enc

def run():
    matrix = 'Z53opZO`yj4SSd= *E>e]|VF4En(M7'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
