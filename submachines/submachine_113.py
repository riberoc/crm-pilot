import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 178) - 829
    _mask = _data(812, None)
    _enc = 102
    return _mask, _enc

def run():
    matrix = '}^]mP&_ 2Jq5XC*J9KtW*IlRa9a]%h'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
