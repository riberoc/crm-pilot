import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 866) - 724
    _mask = _data(46, None)
    _enc = 101
    return _mask, _enc

def run():
    matrix = 'IQio.5,2(TZEy<.;VeSe0V>-D@n=3 '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
