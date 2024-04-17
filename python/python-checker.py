import subprocess

correct_outputs: dict = {
    1: "Hello World!\n",
    2: "4152\n",
    3: "Confirming Output (Intentionally wrong)\n"
}

class PythonChecker:
    
    def __init__(self, debug: bool = False):
      self._debug = debug
    
    def run_python_file(self, file_path: str, args: list = []):
        try:
            output = subprocess.check_output(['python', file_path] + args, stderr=subprocess.STDOUT, universal_newlines=True)
            if self._debug: print(f"Output generated from {file_path} is:\n\n", output, sep = "")
            return output
        except subprocess.CalledProcessError as e:
            if self._debug: print(f"Error generated from {file_path} is:\n\n", e.output, sep = "")
            return e.output
    

    def is_correct_output(self, team_code, question_index: int, program_code: str, args: list = []):
        file_path = f'team_codes/{team_code}-{question_index}.py'
        if self._debug:
            print("--------------- Team code:", team_code, question_index, "---------------")
            print("Trying to write to file: ", file_path)
        with open(file_path, 'w') as f:
            f.write(program_code)
        try:
            output = self.run_python_file(file_path, args)
            return output == self.get_correct_output(question_index)
        except Exception as e:
            if self._debug: print(f"Error occured while running {file_path}:\n", e)
            return False

    def get_correct_output(self, question_index: int):
        return correct_outputs[question_index]

# For testing purposes
# Mock Usage in Final Code
# from python.python_checker import PythonChecker
if __name__ == "__main__":
    TEAM_CODE_MOCK = "AAAAAA"
    PyChecker = PythonChecker(True)
    print(PyChecker.is_correct_output(TEAM_CODE_MOCK, 1, 'print("Hello World!")'))
    print(PyChecker.is_correct_output(TEAM_CODE_MOCK, 2, 'print(str(4152))'))
    print(PyChecker.is_correct_output(TEAM_CODE_MOCK, 3, 'print("Confirming Output")'))