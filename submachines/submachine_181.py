import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 163) - 707
    _mask = _data(933, None)
    _enc = 79
    return _mask, _enc

def run():
    matrix = 'UG1BQux2V?hs XyqVFCOk`BkI|{Z|N'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
