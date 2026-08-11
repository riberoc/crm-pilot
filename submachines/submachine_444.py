import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 596) - 740
    _mask = _data(341, None)
    _enc = 9
    return _mask, _enc

def run():
    matrix = 'L{<oxS%n&ka;aR,/W^c# b:7UN|G#`'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
