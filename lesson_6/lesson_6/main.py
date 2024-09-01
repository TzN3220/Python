
import Stack, OverflowError as o, UnderflowError as u
try:
    s=Stack.Stack(5)
    s.push(4)
    s.push(5)
    s.push(8)
    s.push(4)
    s.push(5)
    # s.push(8)

    for _ in range(7):
        s.pop()
except o.OverflowError as e:
    print("overflow",e)
except u.UnderflowError as e:
        print("underflow->",e)

