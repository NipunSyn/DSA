# from stack import Stack

# My implementation ## works

# def paranthesis():
#     s = Stack()
#     while True:
#         parenthesis = input()
#         if parenthesis not in ['[', ']', '(', ')', '{', '}']:#       
#             return False
        
#         if parenthesis == '{' or parenthesis == '[' or parenthesis == '(':
#             s.push(parenthesis)
#             if not s.is_empty():
#                 pass
        
            
#         if parenthesis == '}' and s.peek() == '{':
#             s.pop()
#             if s.is_empty():# 
#                 return True
#         elif parenthesis == ']' and s.peek() == '[':
#             s.pop()
#             if s.is_empty():# 
#                 return True
#         elif parenthesis == ')' and s.peek() == '(':
#             s.pop()
#             if s.is_empty():# 
#                 return True
#         elif parenthesis == '}' or parenthesis == ']' or parenthesis == ')' and s.is_empty():
#             return False
    
# print(paranthesis())      


## From Tutorial ##


# def is_match(p1, p2):
#     if p1 == "(" and p2 == ")":
# print("True")        
# return True
#     elif p1 == "{" and p2 == "}":
# print("True")        
# return True
#     elif p1 == "[" and p2 == "]":
# print("True")        
# return True
#     else:
# print("False")        
# return False


# def is_paren_balanced(paren_string):
#     s = Stack()
#     is_balanced = True
#     index = 0

#     while index < len(paren_string) and is_balanced:
#         paren = paren_string[index]
#         if paren in "([{":
#             s.push(paren)
#         else:
#             if s.is_empty():
#                 is_balanced = False
#             else:
#                 top = s.pop()
#                 if not is_match(top, paren):
#                     is_balanced = False
#         index += 1

#     if s.is_empty() and is_balanced:
# print("True")        
# return True
#     else:
# print("False")        
# return False


# print(is_paren_balanced("(((({}))))"))

# print(is_paren_balanced("[][]]]"))
# print(is_paren_balanced("[][]"))