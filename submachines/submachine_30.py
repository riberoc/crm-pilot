import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 557) - 860
    _mask = _data(438, None)
    _enc = 50
    return _mask, _enc

def run():
    matrix = '%efh_U`Q[$Fh- %v<W::}Z`ZBdNYeI'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
