import socket
import re

def tokenize(expression):
    """Extracts numbers and operators correctly from an expression."""
    try:
        tokens = re.findall(r'-?\d+\.?\d*|[+\-*/%]', expression)
        return tokens
    except Exception as e:
        return f"Error: Invalid expression ({str(e)})"

def perform_operations(operands, operators):
    """Performs operations following BODMAS manually."""
    try:
        while '*' in operators or '/' in operators or '%' in operators:
            for i in range(len(operators)):
                if operators[i] in "*/%":
                    if operators[i] == '*':
                        result = operands[i] * operands[i + 1]
                    elif operators[i] == '/':
                        if operands[i + 1] == 0:
                            return "Error: Division by zero"
                        result = operands[i] / operands[i + 1]
                    elif operators[i] == '%':
                        if operands[i + 1] == 0:
                            return "Error: Modulo by zero"
                        result = operands[i] % operands[i + 1]

                    operands[i] = result
                    del operands[i + 1]
                    operators.pop(i)
                    break

        while '+' in operators or '-' in operators:
            for i in range(len(operators)):
                if operators[i] in "+-":
                    if operators[i] == '+':
                        result = operands[i] + operands[i + 1]
                    elif operators[i] == '-':
                        result = operands[i] - operands[i + 1]

                    operands[i] = result
                    del operands[i + 1]
                    operators.pop(i)
                    break

        return operands[0]  
    except Exception as e:
        return f"Error: {str(e)}"

def evaluate_expression(expression):
    """Evaluates a mathematical expression with BODMAS rule."""
    tokens = tokenize(expression)
    if isinstance(tokens, str) and tokens.startswith("Error"):
        return tokens

    operands = []
    operators = []

    for token in tokens:
        if re.match(r'-?\d+\.?\d*', token):  # Check if number (including negatives)
            operands.append(float(token) if '.' in token else int(token))
        elif token in "+-*/%":
            operators.append(token)
        else:
            return "Error: Invalid token encountered"

    if len(operands) - 1 != len(operators):
        return "Error: Mismatched number of operands and operators"

    return perform_operations(operands, operators)

def start_server(host="0.0.0.0", port=11001):
    """Starts the server to handle requests."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}...")
    except Exception as e:
        print(f"Error while setting up server: {e}")
        return

    try:
        client_socket, addr = server_socket.accept()
        print(f"Connected to {addr}")

        while True:
            expression = client_socket.recv(1024).decode().strip()
            if not expression or expression.lower() == "end":
                print("Client disconnected.")
                break

            print(f"Received: {expression}")
            result = evaluate_expression(expression)
            client_socket.send(f"RESULT: {result}".encode())

    except Exception as e:
        print(f"Error during communication: {e}")
    finally:
        client_socket.close()
        server_socket.close()

if __name__ == "__main__":

    start_server()
