import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 210) - 464
    _mask = _data(741, None)
    _enc = 117
    return _mask, _enc

def run():
    matrix = 'gMMK%*w9xRfF,|4P.b O>CfVvf0T!N'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
