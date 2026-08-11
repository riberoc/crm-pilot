import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 742) - 784
    _mask = _data(418, None)
    _enc = 60
    return _mask, _enc

def run():
    matrix = '?DryKw<:tcT$Pm+?js=v6Zv2-1&A!k'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
