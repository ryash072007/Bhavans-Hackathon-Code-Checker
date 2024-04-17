import subprocess
import os


class CChecker:
    def __init__(self, debug: bool = False):
        self._debug = debug

    def compile_file(self, file_path: str, output_name: str):
        try:
            compile_output = subprocess.check_output(
                ["gcc", file_path, "-o", output_name], universal_newlines=True
            )
            if self._debug:
                print(compile_output)
            return output_name + ".exe", None
        except subprocess.CalledProcessError as e:
            if self._debug:
                print(f"Error generated from {file_path} is:\n\n", e.output, sep="")
            return None, e.output

    def get_output(self, output_file, args: list = []):
        try:
            run_output = subprocess.check_output(
                [output_file] + args, universal_newlines=True
            )
            return run_output
        except Exception as e:
            return e
        
    def is_correct_output(self, team_code, question_index: int, program_code: str, args: list = []):
        file_path = f'team_codes/{team_code}-{question_index}.c'
        output_path = f"team_codes/{team_code}-{question_index}"
        if self._debug:
            print("--------------- Team code:", team_code, question_index, "---------------")
            print("Trying to write to file: ", file_path)
        with open(file_path, 'w') as f:
            f.write(program_code)
        try:
            output_file, error = checker.compile_file(file_path, output_path)
            if error:
                return error
            
            code_output = self.get_output(output_file)
            
            print(code_output)
            
        except Exception as e:
            if self._debug: print(f"Error occured while running {file_path}:\n", e)
            return False

if __name__ == "__main__":
    TEAM_CODE_MOCK = "AAAAAA"
    checker = CChecker(True)
