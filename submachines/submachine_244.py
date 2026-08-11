import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 976) - 529
    _mask = _data(379, None)
    _enc = 150
    return _mask, _enc

def run():
    matrix = 'tr@(u^oV.^&[ rFiAjq/emr@k}0$K['
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
