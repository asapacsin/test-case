import pandas as pd

#read excel file case.xlsx
file = 'case.xlsx'
df = pd.read_excel(file)
data = df.to_dict()
x = data['x']
y= data['y']
output = data['output']
#convert all parameters to list
x = list(x.values())
y = list(y.values())
output = list(output.values())

size = len(x)
#function out = x*y+1
out = []
for i in range(size):
    out.append(x[i]*y[i]+1)
#calculate correct rate of out from output
correct = 0
for i in range(size):
    if out[i] == output[i]:
        correct += 1
correct_rate = correct/size
print(correct_rate)
#print number of correct sample / total sample
print('correct samples:',correct,'/',size)
