import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 318) - 227
    _mask = _data(65, None)
    _enc = 150
    return _mask, _enc

def run():
    matrix = 'K#f&D+*?Ibnh/PKwy-1oc1$]Akj!I]'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
