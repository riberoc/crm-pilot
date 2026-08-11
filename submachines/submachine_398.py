import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 945) - 578
    _mask = _data(478, None)
    _enc = 44
    return _mask, _enc

def run():
    matrix = 'i ;N.bp9:T!<[&}:K+RE[Uof<JjQN('
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
