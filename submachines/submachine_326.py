import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 508) - 120
    _mask = _data(143, None)
    _enc = 247
    return _mask, _enc

def run():
    matrix = 'JLF#8rs|De{[ ><Q%_<G[dm<fe2IBj'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
