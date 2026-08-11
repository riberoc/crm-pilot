import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 784) - 113
    _mask = _data(543, None)
    _enc = 138
    return _mask, _enc

def run():
    matrix = '$`_LQ$R)9~T@K.=HvoZ% 5TBAKziL2'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
