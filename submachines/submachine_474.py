import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 522) - 851
    _mask = _data(403, None)
    _enc = 78
    return _mask, _enc

def run():
    matrix = '!3nh|OaqyM<-!d(KkC3SAw~ge6GS},'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
