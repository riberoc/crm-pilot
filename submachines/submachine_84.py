import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 548) - 364
    _mask = _data(858, None)
    _enc = 20
    return _mask, _enc

def run():
    matrix = '6V5cg2 =f>Qtdm@a<0Gh}&9&y;]Jni'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
