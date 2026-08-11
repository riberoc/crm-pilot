import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 782) - 425
    _mask = _data(425, None)
    _enc = 235
    return _mask, _enc

def run():
    matrix = '+$BX&b0{FhK9Kb|6dS_+h U$3bJM(:'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
