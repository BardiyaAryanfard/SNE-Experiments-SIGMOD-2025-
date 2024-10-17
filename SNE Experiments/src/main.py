import math
import sys

from src.algorithms.EMMMVZ.CountSketch import CountSketch
from src.algorithms.EMMMVZ.distinct_elements_general import DistinctElementsGeneral, SingleDistinctElementsGeneral
from src.algorithms.EMMMVZ.grouping_sum import GroupingSum
from src.algorithms.EMMMVZ.low_frequency_elements_small import LowFrequencySmall
from src.non_private.norms import Norms
from src.util.BCM_optimized import BCMOpt
from src.util.Laplace import Laplace
from src.util.input import Input


# for inp in range(10):
#     data = Input.read_input(open('files/input' + str(inp) + '.txt', 'r'))
#     T = data.T
#     n = data.n
#     F = []
#     last = 0
#     f = []
#     for i in range(n):
#         f.append(0)
#         F.append(BCMOpt(T, 1))
#     for i in range(data.T):
#         upd = data.stream.get(i)
#         F[upd.element].update(1)
#         f[upd.element] += 1
#     for i in range(n):
#         print(str(i)+': '+str(f[i])+' vs. '+str(F[i].get_real_sum()))
#     print("_____________________")
#
def generate_input(test, ID, div):
    name = str(test) + '_' + str(ID) + '_' + 'logT'
    f = open('script_input' + name + '.txt', 'w')
    f.write('Artificial-powerlaw-' + str(test) + '\n' + str(0) + '\n' + str(ID))
    f.close()


def generate_script(test, ID):
    name = str(test) + '_' + str(ID) + '_' + 'logT'
    file = open('scriptlm10_1_logT.sh', 'r')
    lines = file.readlines()  # Read all lines
    lines = [line.strip() for line in lines]
    lines[6] = '#SBATCH --job-name=PL' + name + 'lm'
    lines[7] = '#SBATCH --output=Artificial-powerlaw-' + name + '-output.txt'
    lines[42] = 'python judge.py < script_input' + name + '.txt'
    new_file = open('scriptlm' + name + '.sh', 'w')
    for line in lines:
        new_file.write(line + '\n')
    new_file.close()


# Function to replace all occurrences of '\r\n' with '\n' in a file
def replace_line_endings(file_path):
    try:
        # Open the file in binary mode and read its contents
        with open(file_path, 'rb') as file:
            content = file.read()

        # Replace \r\n with \n
        updated_content = content.replace(b'\r\n', b'\n')

        # Write the updated content back to the file in binary mode
        with open(file_path, 'wb') as file:
            file.write(updated_content)

        print(f"Line endings successfully replaced in '{file_path}'.")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
file_path = 'example.sh'  # Replace with your script file path
replace_line_endings(file_path)

# for test in [10, 11, 12]:
#     for ID in [1, 2, 3, 4, 5]:
#         div = 0
#         generate_input(test, ID, div)
#         generate_script(test, ID, div)
#         replace_line_endings('scriptlm' + str(test) + '_' + str(ID) + '_logT' + '.sh')
