import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 127) - 272
    _mask = _data(395, None)
    _enc = 234
    return _mask, _enc

def run():
    matrix = ',8~NuA.72)sp4S vXz(lRz%Pf.C#EV'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
