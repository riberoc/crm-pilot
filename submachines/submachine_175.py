import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 162) - 555
    _mask = _data(575, None)
    _enc = 121
    return _mask, _enc

def run():
    matrix = '%m>O4+nP(XE vX3foZ:N!:[`er?/x?'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
