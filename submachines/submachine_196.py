import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 391) - 179
    _mask = _data(251, None)
    _enc = 198
    return _mask, _enc

def run():
    matrix = 'H[&DHW$j)GwM]$S Rtaw9smAG0-mC]'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
