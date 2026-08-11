import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 602) - 378
    _mask = _data(45, None)
    _enc = 246
    return _mask, _enc

def run():
    matrix = '_x]rjso%rn1 sYcfU`LsLaS|z!tGo#'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
