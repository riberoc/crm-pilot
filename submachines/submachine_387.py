import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 442) - 445
    _mask = _data(808, None)
    _enc = 200
    return _mask, _enc

def run():
    matrix = '%,JF#T~|Vyrigg:K=e!m=m453.$H[ '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
