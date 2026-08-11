import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 333) - 153
    _mask = _data(33, None)
    _enc = 216
    return _mask, _enc

def run():
    matrix = 'cp.sODxMU+g :-Wo[{-2+lll~{r~))'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
