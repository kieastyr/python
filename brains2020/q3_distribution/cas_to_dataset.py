import csv

inputname = "data/smiles_cas_N6512.smi"
outputname_in = "sample/sample1.in"
outputname_out = "sample/sample1.out"
in_data = []
out_data = []
with open(inputname, "r") as f:
    line = csv.reader(f)
    for l in line:
        in_data.append([l[0]])
        out_data.append([l[2]])

with open(outputname_in, "w") as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(in_data)

with open(outputname_out, "w") as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(out_data)
