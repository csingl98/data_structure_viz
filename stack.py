#from linked_lists import LinkedList

class Stack():
    def __init__(self) -> None:
        self.items = []

    def pop(self):
        if self.isEmpty() == True:
            return None

        removed = self.items[len(self.items) - 1]
        self.items = self.items[:-1]

        return removed

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[len(self.items) - 1]

    def isEmpty(self):
        return self.items == []


def main():
    #reverse a string
    input_string = "abcedfg"
    string_stack = Stack()
    [string_stack.push(s) for s in input_string]
    reverse_string = []

    while string_stack.isEmpty() != True:
        reverse_string.append(string_stack.pop())

    final = ''.join(reverse_string)

    #balanced expressions
    #if a string has something like brackets, parenthesis or quotation marks which require an opener and a closer
    # a string is considered balanced if both are present. Unbalanced if one is missing

    #iterate over string

    #if it is a opener append to stack, if it is regular, ignore

    #when you come to a closer, reverse through stack and return false if it does not match the previous

    expressions = {}
    expressions["["] = "]"
    expressions["{"] = "}"
    expressions["<"] = ">"
    expressions["("] = ")"

    input_string = "[who]"
    stack_checker = Stack()
    for s in input_string:
        
        if s in list(expressions.keys()):
            stack_checker.push(s)
        elif s in list(expressions.values()):
            last_exp = stack_checker.pop()

            if expressions[last_exp] != s:
                raise SyntaxError()

#MOSH'S SOLUTION
class Expression():
    def __init__(self, string) -> None:
        self.string = string
        self.brackets = {}

        self.brackets["["] = "]"
        self.brackets["{"] = "}"
        self.brackets["<"] = ">"
        self.brackets["("] = ")"
    
    def isBalanced(self):
        stack = Stack()
        for s in self.string:

            if s in ["(", "[", "{"]:
                stack.push(s)
            elif s in [")", "]", "}"]:
                if stack.isEmpty(): return False
                
                top = stack.pop()
                if self.BracketMatch(top, s) != True: return False

        return stack.isEmpty()

    def BracketMatch(self, left, right):
        #he wrote code to check if left and right match using a ton of if statements, I prefer my dict so I will use that instead
        return self.brackets[left] == right







        

