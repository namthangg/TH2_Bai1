import re
import itertools

# Hàm kiểm tra tính hợp lệ của biểu thức logic
def is_valid_expression(expression):
    valid_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz∧∨→¬() ')
    if not all(c in valid_chars for c in expression):
        return False
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

def evaluate_expression(expression, values):
    expression = expression.replace('∧', 'and').replace('∨', 'or').replace('¬', 'not').replace('→', '<=')
    try:
        return eval(expression, {"__builtins__": None}, values)
    except Exception as e:
        return False

# Hàm chính tạo bảng chân trị
def generate_truth_table(expression):
    if not is_valid_expression(expression):
        print("Biểu thức không hợp lệ.")
        return
    variables = re.findall(r'[A-Za-z]+', expression)
    variables = sorted(set(variables))
    combinations = list(itertools.product([True, False], repeat=len(variables)))
    header = "\t".join(variables) + "\tKết quả"
    print(header)
    for combination in combinations:
        values = dict(zip(variables, combination))
        result = evaluate_expression(expression, values)
        row = "\t".join("T" if values[var] else "F" for var in variables)
        print(f"{row}\t{'T' if result else 'F'}")
# Gọi hàm nhập biểu thức và hiển thị bảng chân trị
def main():
    expression = input("Nhập biểu thức logic: ")
    generate_truth_table(expression)
# Chạy chương trình
main()
