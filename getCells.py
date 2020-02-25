import os

# Generic function to return cell object containing sections 
def Cell(path = None):
	owd = os.getcwd()
	os.chdir(path)
	from cell_utils import Utils
	cell = Utils().cell
	os.chdir(owd)
	return cell

def activeCell(path = None):
	owd = os.getcwd()
	os.chdir(path)
	from active_cell_utils import Utils
	cell = Utils().cell
	os.chdir(owd)
	return cell

def KoleCell():
	owd = os.getcwd()
	os.chdir('./Kole')
	from neuron import h, init
	h.load_file("/usr/local/nrn//share/nrn/lib/hoc/stdrun.hoc")
	h.load_file('cellTemplate.hoc')
	cell = h.KoleCell()
	os.chdir(owd)
	return cell

def AckerAnticCell():
	owd = os.getcwd()
	os.chdir('./AckerAntic')
	# from neuron import h, init
	# h.load_file("/usr/local/nrn//share/nrn/lib/hoc/stdrun.hoc")
	# exec(open('./cells/eeeD.py').read())
	import sys 
	sys.path.insert(1, './cells/')
	from eeeD import MakeCell
	cell = MakeCell()
	os.chdir(owd)
	return cell

def NeymotinCell():
	owd = os.getcwd()
	os.chdir('./Neymotin')
	from neuron import h, init
	h.load_file("./cells/PTcell.hoc")
	ihMod2str = {'harnett': 1, 'kole': 2, 'migliore': 3}
	cell = h.PTcell(ihMod2str['migliore'], 14*2)
	os.chdir(owd)
	return cell

def HayCell():
	owd = os.getcwd()
	os.chdir('./Hay')
	from neuron import h, init
	h.load_file("/usr/local/nrn//share/nrn/lib/hoc/stdrun.hoc")
	h.load_file('import3d.hoc')
	h.load_file('./models/L5PCbiophys3.hoc') # BAP version
	h.load_file('./models/L5PCtemplate.hoc')
	morphology_file = './morphologies/cell1.asc'
	cell = h.L5PCtemplate(morphology_file)
	os.chdir(owd)
	return cell