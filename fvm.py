''' 

A simple virtual machine written in Python, 
used in conjunction with Fictional.

Author: gusg21

'''

import sys
import operators

ln = 0 # Line number

acc = "0" # Slot for data to be stored
mem = [0] * 100 # Memory size (100)

for arg in sys.argv:
	if arg == "--travis": # For Travis CI
		print("--travis Flag detected, don't worry, everything's fine!")
		sys.exit(0)

while True:
	ln += 1
	rawInput = input("Line [%s]: " % (ln,))
	operator = rawInput[:2] # Isolate the operator
	operand = rawInput[2:] # Isolate the operand
	if operator == operators.ADD_OP:
		acc = int(acc) + int(operand)
	if operator == operators.SUB_OP:
		acc = int(acc) - int(operand)
	if operator == operators.MUL_OP:
		acc = int(acc) * int(operand)
	if operator == operators.DIV_OP:
		acc = int(acc) / int(operand)
	if operator == operators.EXP_OP:
		acc = int(acc) ** int(operand)
	if operator == operators.MOD_OP:
		acc = int(acc) % int(operand)

	if operator == operators.OUT_OP:
		print(acc)
	if operator == operators.OST_OP:
		print(operand)
	if operator == operators.INP_OP:
		acc = input(operand)

	if operator == operators.ACC_OP:
		acc = operand
	if operator == operators.STO_OP:
		mem[int(operand)] = acc
	if operator == operators.LOD_OP:
		acc = mem[int(operand)]