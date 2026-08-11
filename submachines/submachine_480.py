import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 223) - 698
    _mask = _data(844, None)
    _enc = 207
    return _mask, _enc

def run():
    matrix = 'K#qf0UfpNJl#Z].tVGa-e8 F9,I,Vc'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
