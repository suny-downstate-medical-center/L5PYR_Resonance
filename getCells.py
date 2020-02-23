import os

neuronal_model_ids = [485591806]

# Func to download cell files from allen institute, not sure if keeping
def getCells():
	from allensdk.api.queries.biophysical_api import BiophysicalApi

	bp = BiophysicalApi()
	bp.cache_stimulus = False # change to False to not download the large stimulus NWB file

	for neuronal_model_id in neuronal_model_ids:
		os.system('mkdir ' + str(neuronal_model_id))
		bp.cache_data(neuronal_model_id, working_directory=str(neuronal_model_id))
		os.system('cd ' + str(neuronal_model_id) + '; nrnivmodl ./modfiles; cd ../')
		os.system('cp ../471087975/cell_utils.py ' + str(neuronal_model_id))
		os.system('cp ../471087975/cell_template.hoc ' + str(neuronal_model_id))

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
	from neuron import h, init
	h.load_file("/usr/local/nrn//share/nrn/lib/hoc/stdrun.hoc")
	exec(open('./cells/eeeD.py').read())
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