
class AbstractExpression:
    def interpret(self):
        pass

    def __str__(self):
        return "Expression"


class Number(AbstractExpression):
    def __init__(self, value):
        self.value = float(value)

    def interpret(self):
        return self.value

    def __str__(self):
        return str(int(self.value) if self.value.is_integer() else self.value)


class AlgebraExpression(AbstractExpression):
    operator = "?"

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"({self.left} {self.operator} {self.right})"

class Add(AlgebraExpression):
    operator = "+"

    def interpret(self):
        return self.left.interpret() + self.right.interpret()


class Subtract(AlgebraExpression):
    operator = "-"

    def interpret(self):
        return self.left.interpret() - self.right.interpret()


class Multiply(AlgebraExpression):
    operator = "*"

    def interpret(self):
        return self.left.interpret() * self.right.interpret()


class Divide(AlgebraExpression):
    operator = "/"

    def interpret(self):
        return self.left.interpret() / self.right.interpret()

if __name__ == "__main__":
    target ="3 + 5 - 2 * 7 / 5 + 11"
    
    tokens = target.split(" ")
    expressions = []
    
    for i in range(len(tokens)):
        if i == 0:
            expressions.append(Number(tokens[i]))
        elif tokens[i] == "+":
            expressions.append(Add(expressions.pop(), Number(tokens[i+1])))
            print(f"Added {tokens[i+1]} to the expression")
            print(f"Current expression: {expressions[-1]}")
            
        elif tokens[i] == "-":
            expressions.append(Subtract(expressions.pop(), Number(tokens[i+1])))
            print(f"Subtracted {tokens[i+1]} from the expression")
            print(f"Current expression: {expressions[-1]}")
            
        elif tokens[i] == "*":
            expressions.append(Multiply(expressions.pop(), Number(tokens[i+1])))
            print(f"Multiplied {tokens[i+1]} to the expression")
            print(f"Current expression: {expressions[-1]}")
        elif tokens[i] == "/":
            expressions.append(Divide(expressions.pop(), Number(tokens[i+1])))
            print(f"Divided {tokens[i+1]} to the expression")
            print(f"Current expression: {expressions[-1]}")
        
    print(f'tokens = {tokens}')
    print(expressions)
    result = expressions.pop().interpret()
    print(f"Result: {result}")