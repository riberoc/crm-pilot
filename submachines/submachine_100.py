import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 831) - 643
    _mask = _data(495, None)
    _enc = 86
    return _mask, _enc

def run():
    matrix = '3cUT<*VJ84SW(bHtXzcDl2_gEHH d{'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
