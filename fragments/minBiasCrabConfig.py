from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'AE_minBias_3_23_2'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'produce_ntuple_std_ae_xyseed_reduced_pt5_v11_cfg.py'
config.JobType.maxMemoryMB = 4000

config.Data.inputDataset = '/MinBias_TuneCP5_14TeV-pythia8/Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v3/GEN-SIM-DIGI-RAW'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.outLFNDirBase = '/store/user/cmantill/HGCAL/AE_Jun11/'
config.Data.unitsPerJob = 10

config.Data.publication = False
config.Site.storageSite = 'T3_US_FNALLPC'

