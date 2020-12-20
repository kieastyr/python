from rdkit import Chem

# smile = input()
smile = "COC(=O)[C@]12O[C@@]1(C)[C@@](O)(NC2=O)C(C)C"
m = Chem.MolFromSmiles(smile)
m_h = Chem.AddHs(m)
patt = Chem.MolFromSmarts('C')
print(m.GetSubstructMatches(patt))
