import os
import sys

active_model_ids = [497229117, 491766131, 497232312, 485591806,
		497232419, 497232429, 496930324, 497232564, 497232839, 497232946,
		497233049, 497233139, 497233307, 497229124]

class allenCell:
	def __init__(self):
		self.basal = []
		self.apical = []
		self.soma = []
		self.axon = []

	def generate_cell(self, h):
		for sec in h.soma:
			self.soma.append(sec)
		for sec in h.apic:
			self.apical.append(sec)
		for sec in h.dend:
			self.basal.append(sec)
		for sec in h.axon:
			self.axon.append(sec)

def GetAllenCells(neuronal_model_ids):

	from allensdk.api.queries.biophysical_api import BiophysicalApi

	bp = BiophysicalApi()
	bp.cache_stimulus = False # change to True to download the large stimulus NWB file

	for neuronal_model_id in neuronal_model_ids:
		os.system('mkdir ' + str(neuronal_model_id))
		bp.cache_data(neuronal_model_id, working_directory=str(neuronal_model_id))
		os.system('cd ' + str(neuronal_model_id) + '; nrnivmodl ./modfiles; cd ../')

def AllenCell(path = None):
	owd = os.getcwd()
	os.chdir(path)
	sys.path.append('/usr/local/python/')
	from allensdk.model.biophys_sim.config import Config                                         
	from allensdk.model.biophysical import utils as Utils # this is basically "implied" in the tutorial                                   
	description = Config().load('manifest.json')  
	manifest = description.manifest                                                              
	morphology_path = description.manifest.get_path('MORPHOLOGY') 
	utils = Utils.create_utils(description, model_type='Biophysical - all active') # this is insane - help doc says ALL_ACTIVE_TYPE or PERISOMATIC_TYPE for model_type
	h = utils.h
	utils.generate_morphology(morphology_path) # in tutorial, they instead use mophology_path.encode('ascii','ignore')
	utils.load_cell_parameters()
	cell = allenCell()
	cell.generate_cell(h)
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
	import sys 
	sys.path.insert(1, './cells/')
	from eeeD import MakeCell
	cell = MakeCell()
	os.chdir(owd)
	return cell

def NeymotinCell(slope=14*2):
	owd = os.getcwd()
	os.chdir('./Neymotin')
	from neuron import h, init
	h.load_file("./cells/PTcell.hoc")
	ihMod2str = {'harnett': 1, 'kole': 2, 'migliore': 3}
	cell = h.PTcell(ihMod2str['migliore'], slope)
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