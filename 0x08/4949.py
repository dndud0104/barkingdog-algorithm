a = input()
while a != '.':
    stack = []
    
    for word in a:
        if word == '(' or word == '[':
            stack.append(word)
        elif (word == ')' or word == ']') and not stack:
            stack.append(word)
            break
        elif stack and word == ')' and stack[-1] == '[':
            break
        elif stack and word == ']' and stack[-1] == '(':
            break
        elif stack and word == ')' and stack[-1] == '(':
            stack.pop()
        elif stack and word == ']' and stack[-1] == '[':
            stack.pop()
                 
    if not stack:
        print('yes')
    else:
        print('no')
        
    a = input()
