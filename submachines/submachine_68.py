import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 191) - 599
    _mask = _data(586, None)
    _enc = 142
    return _mask, _enc

def run():
    matrix = '?q}L%WO,eAIc_*N{ ]X=uKvZ,(/q,>'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
