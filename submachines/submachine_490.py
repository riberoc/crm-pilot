import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 517) - 703
    _mask = _data(268, None)
    _enc = 91
    return _mask, _enc

def run():
    matrix = '%!wpngzhVvUC=?M7# k[Fasi2Oeu!}'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
