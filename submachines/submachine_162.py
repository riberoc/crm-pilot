import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 364) - 597
    _mask = _data(586, None)
    _enc = 201
    return _mask, _enc

def run():
    matrix = '2M1`u+S3#$&}bBXOFRh1`5(bkT^,p.'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
