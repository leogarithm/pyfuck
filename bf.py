"""
    file: bf.py
    author: Léo Giroud
    last modified: 14/01/2021
    description: a function to evaluate Brainfuck expressions
"""

import string

def evaluate(script: str, inp="", print_output=False) -> str:
    """
        Evaluates a Brainfuck expression.
        :param script: A Brainfuck expression to be evaluated
        :param inp: Input for the expression
        :param print_output: Prints the output directly to console
        :type script: str
        :type inp: str
        :type print_output: bool
        :return: The output computed by script
        :rtype: str
    """
    bf_chars = "+-<>.,[]"
    all_nonbf_chars = string.printable.translate(string.printable.maketrans("", "", bf_chars))

    script = script.translate(script.maketrans("", "", all_nonbf_chars))
    byte = 256
    end = len(script) - 1

    pt = 0
    pt_script = 0
    pt_inp = 0
    pt_loop = 0
    
    cells = { 0: 0 }
    outp = ""
    
    while 0 <= pt_script <= end:
        c = script[pt_script]
        if "+" in c:
            cells[pt] += 1
            if cells[pt] >= byte:
                cells[pt] = 0
        elif "-" in c:
            cells[pt] -= 1
            if cells[pt] < 0:
                cells[pt] = byte - 1
        elif ">" in c:
            pt += 1
            if pt not in cells:
                cells[pt] = 0
        elif "<" in c:
            pt -= 1
            if pt not in cells:
                cells[pt] = 0
        elif "," in c:
            if pt_inp < len(inp):
                cells[pt] = ord(inp[pt_inp])
                pt_inp += 1
            else:
                cells[pt] = 0
        elif "." in c:
            outp += chr(cells[pt])
        elif "[" in c:
            if cells[pt] == 0:
                pt_loop = 1
                while pt_loop > 0 and 0 <= pt_script <= end:
                    pt_script += 1
                    c = script[pt_script]
                    if "[" in c:
                        pt_loop += 1
                    elif "]" in c:
                        pt_loop -= 1
        elif "]" in c:
            if cells[pt] != 0:
                pt_loop = 1
                while pt_loop > 0 and 0 <= pt_script <= end:
                    pt_script -= 1
                    c = script[pt_script]
                    if "]" in c:
                        pt_loop += 1
                    elif "[" in c:
                        pt_loop -= 1
        
        pt_script += 1

    if print_output:
        print(outp)

    return outp