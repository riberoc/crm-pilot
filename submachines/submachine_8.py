import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 100) - 759
    _mask = _data(771, None)
    _enc = 98
    return _mask, _enc

def run():
    matrix = '3JtpI,||MtL67ouG0IaM:t`aD:g7o#'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
