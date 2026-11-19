###
# Checks if brackets in an expression are correctly matched, using a stack
#
import queue

def brackets_ok(expression):
    stack = queue.LifoQueue()
    opening = "({["
    closing = ")}]"
    pairs = {")": "(", "}": "{", "]": "["}    # jaki otwierający pasuje do jakiego zamykającego

    for char in expression:
        if char in opening:
            stack.put(char)
        elif char in closing:
            if stack.empty():
                return False               # zamykający bez otwierającego - źle
            top = stack.get()
            if top != pairs[char]:
                return False               # nie pasuje do siebie - źle

    return stack.empty()    # na koniec stos MUSI być pusty (wszystko domknięte)

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"
expression2 = "[(2+3]/4)"
expression3 = "(2-3*4+(5/6)"

print(f'{expression1}: {brackets_ok(expression1)}')
print(f'{expression2}: {brackets_ok(expression2)}')
print(f'{expression3}: {brackets_ok(expression3)}')