import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 196) - 806
    _mask = _data(841, None)
    _enc = 114
    return _mask, _enc

def run():
    matrix = 'FUqzkLi}sK;?jftl-HsQ- G_qf;/hz'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
