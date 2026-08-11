import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 118) - 506
    _mask = _data(517, None)
    _enc = 112
    return _mask, _enc

def run():
    matrix = "U,VvD7?3r'r~&W[Q^c3E_*Ui8h!tQm"
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
