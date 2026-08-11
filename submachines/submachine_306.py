import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 366) - 772
    _mask = _data(693, None)
    _enc = 216
    return _mask, _enc

def run():
    matrix = "~x^N_TjILKw;*6g'XlnlT.`IIrCR6m"
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
