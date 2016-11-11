import FWCore.ParameterSet.Config as cms

process = cms.Process("MINIAODNTUPLEDUMP")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(''),
    secondaryFileNames = cms.untracked.vstring(),
    skipEvents = cms.untracked.uint32(0)
)
process.CondDB = cms.PSet(
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    connect = cms.string('')
)

process.CondDBSetup = cms.PSet(
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    )
)

process.MicroEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_slimmedPhotons_*_*', 
        'keep *_slimmedElectrons_*_*', 
        'keep *_slimmedMuons_*_*', 
        'keep *_slimmedTaus_*_*', 
        'keep *_slimmedTausBoosted_*_*', 
        'keep *_slimmedJets_*_*', 
        'keep *_slimmedJetsAK8_*_*', 
        'keep *_slimmedJetsPuppi_*_*', 
        'keep *_slimmedMETs_*_*', 
        'keep *_slimmedMETsNoHF_*_*', 
        'keep *_slimmedMETsPuppi_*_*', 
        'keep *_slimmedSecondaryVertices_*_*', 
        'keep *_slimmedJetsAK8PFCHSSoftDropPacked_SubJets_*', 
        'keep *_slimmedJetsAK8PFPuppiSoftDropPacked_SubJets_*', 
        'keep recoPhotonCores_reducedEgamma_*_*', 
        'keep recoGsfElectronCores_reducedEgamma_*_*', 
        'keep recoConversions_reducedEgamma_*_*', 
        'keep recoSuperClusters_reducedEgamma_*_*', 
        'keep recoCaloClusters_reducedEgamma_*_*', 
        'keep EcalRecHitsSorted_reducedEgamma_*_*', 
        'drop *_*_caloTowers_*', 
        'drop *_*_pfCandidates_*', 
        'drop *_*_genJets_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep *_offlineSlimmedPrimaryVertices_*_*', 
        'keep patPackedCandidates_packedPFCandidates_*_*', 
        'keep *_bunchSpacingProducer_*_*', 
        'keep double_fixedGridRhoAll__*', 
        'keep double_fixedGridRhoFastjetAll__*', 
        'keep double_fixedGridRhoFastjetAllCalo__*', 
        'keep double_fixedGridRhoFastjetCentral_*_*', 
        'keep double_fixedGridRhoFastjetCentralCalo__*', 
        'keep double_fixedGridRhoFastjetCentralChargedPileUp__*', 
        'keep double_fixedGridRhoFastjetCentralNeutral__*', 
        'keep *_selectedPatTrigger_*_*', 
        'keep patPackedTriggerPrescales_patTrigger__*', 
        'keep patPackedTriggerPrescales_patTrigger_l1max_*', 
        'keep patPackedTriggerPrescales_patTrigger_l1min_*', 
        'keep *_l1extraParticles_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_gtStage2Digis__*', 
        'keep *_gmtStage2Digis_Muon_*', 
        'keep *_caloStage2Digis_Jet_*', 
        'keep *_caloStage2Digis_Tau_*', 
        'keep *_caloStage2Digis_EGamma_*', 
        'keep *_caloStage2Digis_EtSum_*', 
        'keep *_TriggerResults_*_HLT', 
        'keep *_TriggerResults_*_*', 
        'keep patPackedCandidates_lostTracks_*_*', 
        'keep HcalNoiseSummary_hcalnoise__*', 
        'keep recoCSCHaloData_CSCHaloData_*_*', 
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*')
)

process.MicroEventContentMC = cms.PSet(
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_slimmedPhotons_*_*', 
        'keep *_slimmedElectrons_*_*', 
        'keep *_slimmedMuons_*_*', 
        'keep *_slimmedTaus_*_*', 
        'keep *_slimmedTausBoosted_*_*', 
        'keep *_slimmedJets_*_*', 
        'keep *_slimmedJetsAK8_*_*', 
        'keep *_slimmedJetsPuppi_*_*', 
        'keep *_slimmedMETs_*_*', 
        'keep *_slimmedMETsNoHF_*_*', 
        'keep *_slimmedMETsPuppi_*_*', 
        'keep *_slimmedSecondaryVertices_*_*', 
        'keep *_slimmedJetsAK8PFCHSSoftDropPacked_SubJets_*', 
        'keep *_slimmedJetsAK8PFPuppiSoftDropPacked_SubJets_*', 
        'keep recoPhotonCores_reducedEgamma_*_*', 
        'keep recoGsfElectronCores_reducedEgamma_*_*', 
        'keep recoConversions_reducedEgamma_*_*', 
        'keep recoSuperClusters_reducedEgamma_*_*', 
        'keep recoCaloClusters_reducedEgamma_*_*', 
        'keep EcalRecHitsSorted_reducedEgamma_*_*', 
        'drop *_*_caloTowers_*', 
        'drop *_*_pfCandidates_*', 
        'drop *_*_genJets_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep *_offlineSlimmedPrimaryVertices_*_*', 
        'keep patPackedCandidates_packedPFCandidates_*_*', 
        'keep *_bunchSpacingProducer_*_*', 
        'keep double_fixedGridRhoAll__*', 
        'keep double_fixedGridRhoFastjetAll__*', 
        'keep double_fixedGridRhoFastjetAllCalo__*', 
        'keep double_fixedGridRhoFastjetCentral_*_*', 
        'keep double_fixedGridRhoFastjetCentralCalo__*', 
        'keep double_fixedGridRhoFastjetCentralChargedPileUp__*', 
        'keep double_fixedGridRhoFastjetCentralNeutral__*', 
        'keep *_selectedPatTrigger_*_*', 
        'keep patPackedTriggerPrescales_patTrigger__*', 
        'keep patPackedTriggerPrescales_patTrigger_l1max_*', 
        'keep patPackedTriggerPrescales_patTrigger_l1min_*', 
        'keep *_l1extraParticles_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_gtStage2Digis__*', 
        'keep *_gmtStage2Digis_Muon_*', 
        'keep *_caloStage2Digis_Jet_*', 
        'keep *_caloStage2Digis_Tau_*', 
        'keep *_caloStage2Digis_EGamma_*', 
        'keep *_caloStage2Digis_EtSum_*', 
        'keep *_TriggerResults_*_HLT', 
        'keep *_TriggerResults_*_*', 
        'keep patPackedCandidates_lostTracks_*_*', 
        'keep HcalNoiseSummary_hcalnoise__*', 
        'keep recoCSCHaloData_CSCHaloData_*_*', 
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_slimmedGenJets*_*_*', 
        'keep patPackedGenParticles_packedGenParticles_*_*', 
        'keep recoGenParticles_prunedGenParticles_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep PileupSummaryInfos_slimmedAddPileupInfo_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep GenLumiInfoHeader_generator_*_*', 
        'keep GenLumiInfoProduct_*_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep GenRunInfoProduct_*_*_*', 
        'keep L1GtTriggerMenuLite_l1GtTriggerMenuLite__*')
)

process.OutALCARECOEcalCalElectron = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalCalZElectron', 
            'pathALCARECOEcalCalWElectron', 
            'pathALCARECOEcalCalZSCElectron')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *EcalRecHit*_*ecalPreshowerRecHit*_*EcalRecHitsES*_*', 
        'drop reco*Clusters_hfEMClusters_*_*', 
        'drop reco*Clusters_pfPhotonTranslator_*_*', 
        'drop *EcalRecHit*_ecalRecHit_*_*', 
        'drop *_*Cleaned_*_*', 
        'drop *_*cleaned*_*_*', 
        'drop *_*Unclean*_*_*', 
        'drop *_*unclean*_*_*', 
        'drop *_*_*Unclean*_*', 
        'drop *_*_*unclean*_*', 
        'keep recoSuperClusters_*_uncleanOnly_*', 
        'drop *_*_multi5x5Barrel*Clusters_*', 
        'drop *_dqmL1ExtraParticles_*_*', 
        'drop recoSuperClusters_mergedSuperClusters_*_*', 
        'keep *CaloCluster*_*alCaIsolatedElectrons*_*alcaCaloCluster*_*')
)

process.OutALCARECOEcalCalElectron_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalCalZElectron', 
            'pathALCARECOEcalCalWElectron', 
            'pathALCARECOEcalCalZSCElectron')
    ),
    outputCommands = cms.untracked.vstring('keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *EcalRecHit*_*ecalPreshowerRecHit*_*EcalRecHitsES*_*')
)

process.OutALCARECOEcalCalWElectron = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalCalWElectron')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *EcalRecHit*_*ecalPreshowerRecHit*_*EcalRecHitsES*_*', 
        'drop reco*Clusters_hfEMClusters_*_*', 
        'drop reco*Clusters_pfPhotonTranslator_*_*', 
        'drop *EcalRecHit*_ecalRecHit_*_*', 
        'drop *_*Cleaned_*_*', 
        'drop *_*cleaned*_*_*', 
        'drop *_*Unclean*_*_*', 
        'drop *_*unclean*_*_*', 
        'drop *_*_*Unclean*_*', 
        'drop *_*_*unclean*_*', 
        'keep recoSuperClusters_*_uncleanOnly_*', 
        'drop *_*_multi5x5Barrel*Clusters_*', 
        'drop *_dqmL1ExtraParticles_*_*', 
        'drop recoSuperClusters_mergedSuperClusters_*_*', 
        'keep *CaloCluster*_*alCaIsolatedElectrons*_*alcaCaloCluster*_*')
)

process.OutALCARECOEcalCalWElectron_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalCalWElectron')
    ),
    outputCommands = cms.untracked.vstring('keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *EcalRecHit*_*ecalPreshowerRecHit*_*EcalRecHitsES*_*')
)

process.OutALCARECOEcalCalZElectron = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalCalZElectron', 
            'pathALCARECOEcalCalZSCElectron')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *EcalRecHit*_*ecalPreshowerRecHit*_*EcalRecHitsES*_*', 
        'drop reco*Clusters_hfEMClusters_*_*', 
        'drop reco*Clusters_pfPhotonTranslator_*_*', 
        'drop *EcalRecHit*_ecalRecHit_*_*', 
        'drop *_*Cleaned_*_*', 
        'drop *_*cleaned*_*_*', 
        'drop *_*Unclean*_*_*', 
        'drop *_*unclean*_*_*', 
        'drop *_*_*Unclean*_*', 
        'drop *_*_*unclean*_*', 
        'keep recoSuperClusters_*_uncleanOnly_*', 
        'drop *_*_multi5x5Barrel*Clusters_*', 
        'drop *_dqmL1ExtraParticles_*_*', 
        'drop recoSuperClusters_mergedSuperClusters_*_*', 
        'keep *CaloCluster*_*alCaIsolatedElectrons*_*alcaCaloCluster*_*')
)

process.OutALCARECOEcalCalZElectron_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalCalZElectron', 
            'pathALCARECOEcalCalZSCElectron')
    ),
    outputCommands = cms.untracked.vstring('keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *EcalRecHit*_*ecalPreshowerRecHit*_*EcalRecHitsES*_*')
)

process.OutALCARECOEcalRecalElectron = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalRecalZElectron', 
            'pathALCARECOEcalRecalZSCElectron', 
            'pathALCARECOEcalRecalWElectron')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *EcalRecHit*_*ecalPreshowerRecHit*_*EcalRecHitsES*_*', 
        'keep *_electronRecalibSCAssociator_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_*Uncalib*_*_*', 
        'drop *_*Unclean*_*_*', 
        'drop *_*unclean*_*_*', 
        'drop *_*_*Unclean*_*', 
        'drop *_*_*unclean*_*')
)

process.OutALCARECOEcalRecalElectron_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalCalZElectron', 
            'pathALCARECOEcalCalWElectron', 
            'pathALCARECOEcalCalZSCElectron')
    ),
    outputCommands = cms.untracked.vstring('keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *EcalRecHit*_*ecalPreshowerRecHit*_*EcalRecHitsES*_*', 
        'keep *_electronRecalibSCAssociator_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_*Uncalib*_*_*')
)

process.OutALCARECOEcalUncalElectron = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalUncalZElectron', 
            'pathALCARECOEcalUncalZSCElectron', 
            'pathALCARECOEcalUncalWElectron')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *EcalRecHit*_*ecalPreshowerRecHit*_*EcalRecHitsES*_*', 
        'keep *_ecalDigis_*_*', 
        'keep *EcalTriggerPrimitiveDigi*_ecalDigis_*_*', 
        'keep *_ecalPreshowerDigis_*_*', 
        'keep *_ecalDetIdToBeRecovered_*_*', 
        'keep reco*Clusters_pfElectronTranslator_*_*', 
        'drop recoCaloClusters_*_*_*', 
        'drop recoSuperClusters_*_*_*', 
        'drop recoPreshowerCluster*_*_*_*', 
        'drop *EcalRecHit*_reducedEcalRecHitsES*_*_*', 
        'drop *EcalRecHit*_*_*_*', 
        'keep reco*Clusters_pfElectronTranslator_*_*')
)

process.OutALCARECOEcalUncalElectron_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalCalZElectron', 
            'pathALCARECOEcalCalWElectron', 
            'pathALCARECOEcalCalZSCElectron')
    ),
    outputCommands = cms.untracked.vstring('keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *EcalRecHit*_*ecalPreshowerRecHit*_*EcalRecHitsES*_*', 
        'keep *_ecalDigis_*_*', 
        'keep *EcalTriggerPrimitiveDigi*_ecalDigis_*_*', 
        'keep *_ecalPreshowerDigis_*_*', 
        'keep *_ecalDetIdToBeRecovered_*_*', 
        'keep reco*Clusters_pfElectronTranslator_*_*')
)

process.OutALCARECOEcalUncalWElectron = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalUncalWElectron')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *EcalRecHit*_*ecalPreshowerRecHit*_*EcalRecHitsES*_*', 
        'keep *_ecalDigis_*_*', 
        'keep *EcalTriggerPrimitiveDigi*_ecalDigis_*_*', 
        'keep *_ecalPreshowerDigis_*_*', 
        'keep *_ecalDetIdToBeRecovered_*_*', 
        'keep reco*Clusters_pfElectronTranslator_*_*', 
        'drop recoCaloClusters_*_*_*', 
        'drop recoSuperClusters_*_*_*', 
        'drop recoPreshowerCluster*_*_*_*', 
        'drop *EcalRecHit*_reducedEcalRecHitsES*_*_*', 
        'drop *EcalRecHit*_*_*_*', 
        'keep reco*Clusters_pfElectronTranslator_*_*')
)

process.OutALCARECOEcalUncalWElectron_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalUncalWElectron')
    ),
    outputCommands = cms.untracked.vstring('keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *EcalRecHit*_*ecalPreshowerRecHit*_*EcalRecHitsES*_*', 
        'keep *_ecalDigis_*_*', 
        'keep *EcalTriggerPrimitiveDigi*_ecalDigis_*_*', 
        'keep *_ecalPreshowerDigis_*_*', 
        'keep *_ecalDetIdToBeRecovered_*_*', 
        'keep reco*Clusters_pfElectronTranslator_*_*')
)

process.OutALCARECOEcalUncalZElectron = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalUncalZElectron', 
            'pathALCARECOEcalUncalZSCElectron')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *EcalRecHit*_*ecalPreshowerRecHit*_*EcalRecHitsES*_*', 
        'keep *_ecalDigis_*_*', 
        'keep *EcalTriggerPrimitiveDigi*_ecalDigis_*_*', 
        'keep *_ecalPreshowerDigis_*_*', 
        'keep *_ecalDetIdToBeRecovered_*_*', 
        'keep reco*Clusters_pfElectronTranslator_*_*', 
        'drop recoCaloClusters_*_*_*', 
        'drop recoSuperClusters_*_*_*', 
        'drop recoPreshowerCluster*_*_*_*', 
        'drop *EcalRecHit*_reducedEcalRecHitsES*_*_*', 
        'drop *EcalRecHit*_*_*_*', 
        'keep reco*Clusters_pfElectronTranslator_*_*')
)

process.OutALCARECOEcalUncalZElectron_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalUncalZElectron', 
            'pathALCARECOEcalUncalZSCElectron')
    ),
    outputCommands = cms.untracked.vstring('keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *EcalRecHit*_*ecalPreshowerRecHit*_*EcalRecHitsES*_*', 
        'keep *_ecalDigis_*_*', 
        'keep *EcalTriggerPrimitiveDigi*_ecalDigis_*_*', 
        'keep *_ecalPreshowerDigis_*_*', 
        'keep *_ecalDetIdToBeRecovered_*_*', 
        'keep reco*Clusters_pfElectronTranslator_*_*')
)

process.TrackAssociatorParameterBlock = cms.PSet(
    TrackAssociatorParameters = cms.PSet(
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        accountForTrajectoryChangeCalo = cms.bool(False),
        dREcal = cms.double(9999.0),
        dREcalPreselection = cms.double(0.05),
        dRHcal = cms.double(9999.0),
        dRHcalPreselection = cms.double(0.2),
        dRMuon = cms.double(9999.0),
        dRMuonPreselection = cms.double(0.2),
        dRPreshowerPreselection = cms.double(0.2),
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        propagateAllDirections = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        truthMatch = cms.bool(False),
        useCalo = cms.bool(False),
        useEcal = cms.bool(True),
        useHO = cms.bool(True),
        useHcal = cms.bool(True),
        useMuon = cms.bool(True),
        usePreshower = cms.bool(False)
    )
)

process.cleaningAlgoConfig = cms.PSet(
    cThreshold_barrel = cms.double(4),
    cThreshold_double = cms.double(10),
    cThreshold_endcap = cms.double(15),
    e4e1Threshold_barrel = cms.double(0.08),
    e4e1Threshold_endcap = cms.double(0.3),
    e4e1_a_barrel = cms.double(0.02),
    e4e1_a_endcap = cms.double(0.02),
    e4e1_b_barrel = cms.double(0.02),
    e4e1_b_endcap = cms.double(-0.0125),
    e6e2thresh = cms.double(0.04),
    ignoreOutOfTimeThresh = cms.double(1000000000.0),
    tightenCrack_e1_double = cms.double(2),
    tightenCrack_e1_single = cms.double(1),
    tightenCrack_e4e1_single = cms.double(2.5),
    tightenCrack_e6e2_double = cms.double(3)
)

process.ecal_digi_parameters = cms.PSet(
    EBCorrNoiseMatrixG01 = cms.vdouble(1.0, 0.73354, 0.64442, 0.58851, 0.55425, 
        0.53082, 0.51916, 0.51097, 0.50732, 0.50409),
    EBCorrNoiseMatrixG06 = cms.vdouble(1.0, 0.70946, 0.58021, 0.49846, 0.45006, 
        0.41366, 0.39699, 0.38478, 0.37847, 0.37055),
    EBCorrNoiseMatrixG12 = cms.vdouble(1.0, 0.71073, 0.55721, 0.46089, 0.40449, 
        0.35931, 0.33924, 0.32439, 0.31581, 0.30481),
    EBdigiCollection = cms.string(''),
    EECorrNoiseMatrixG01 = cms.vdouble(1.0, 0.72698, 0.62048, 0.55691, 0.51848, 
        0.49147, 0.47813, 0.47007, 0.46621, 0.46265),
    EECorrNoiseMatrixG06 = cms.vdouble(1.0, 0.71217, 0.47464, 0.34056, 0.26282, 
        0.20287, 0.17734, 0.16256, 0.15618, 0.14443),
    EECorrNoiseMatrixG12 = cms.vdouble(1.0, 0.71373, 0.44825, 0.30152, 0.21609, 
        0.14786, 0.11772, 0.10165, 0.09465, 0.08098),
    EEdigiCollection = cms.string(''),
    ESdigiCollection = cms.string(''),
    EcalPreMixStage1 = cms.bool(False),
    EcalPreMixStage2 = cms.bool(False),
    UseLCcorrection = cms.untracked.bool(True)
)

process.ecal_pulse_shape_covariances = cms.PSet(
    EBPulseShapeCovariance = cms.vdouble(3.001e-06, 1.233e-05, 0.0, -4.416e-06, -4.571e-06, 
        -3.614e-06, -2.636e-06, -1.286e-06, -8.41e-07, -5.296e-07, 
        0.0, 0.0, 1.233e-05, 6.154e-05, 0.0, 
        -2.2e-05, -2.309e-05, -1.838e-05, -1.373e-05, -7.334e-06, 
        -5.088e-06, -3.745e-06, -2.428e-06, 0.0, 0.0, 
        0.0, 0.0, 0.0, 0.0, 0.0, 
        0.0, 0.0, 0.0, 0.0, 0.0, 
        0.0, -4.416e-06, -2.2e-05, 0.0, 8.319e-06, 
        8.545e-06, 6.792e-06, 5.059e-06, 2.678e-06, 1.816e-06, 
        1.223e-06, 8.245e-07, 5.589e-07, -4.571e-06, -2.309e-05, 
        0.0, 8.545e-06, 9.182e-06, 7.219e-06, 5.388e-06, 
        2.853e-06, 1.944e-06, 1.324e-06, 9.083e-07, 6.335e-07, 
        -3.614e-06, -1.838e-05, 0.0, 6.792e-06, 7.219e-06, 
        6.016e-06, 4.437e-06, 2.385e-06, 1.636e-06, 1.118e-06, 
        7.754e-07, 5.556e-07, -2.636e-06, -1.373e-05, 0.0, 
        5.059e-06, 5.388e-06, 4.437e-06, 3.602e-06, 1.917e-06, 
        1.322e-06, 9.079e-07, 6.529e-07, 4.752e-07, -1.286e-06, 
        -7.334e-06, 0.0, 2.678e-06, 2.853e-06, 2.385e-06, 
        1.917e-06, 1.375e-06, 9.1e-07, 6.455e-07, 4.693e-07, 
        3.657e-07, -8.41e-07, -5.088e-06, 0.0, 1.816e-06, 
        1.944e-06, 1.636e-06, 1.322e-06, 9.1e-07, 9.115e-07, 
        6.062e-07, 4.436e-07, 3.422e-07, -5.296e-07, -3.745e-06, 
        0.0, 1.223e-06, 1.324e-06, 1.118e-06, 9.079e-07, 
        6.455e-07, 6.062e-07, 7.217e-07, 4.862e-07, 3.768e-07, 
        0.0, -2.428e-06, 0.0, 8.245e-07, 9.083e-07, 
        7.754e-07, 6.529e-07, 4.693e-07, 4.436e-07, 4.862e-07, 
        6.509e-07, 4.418e-07, 0.0, 0.0, 0.0, 
        5.589e-07, 6.335e-07, 5.556e-07, 4.752e-07, 3.657e-07, 
        3.422e-07, 3.768e-07, 4.418e-07, 6.142e-07),
    EEPulseShapeCovariance = cms.vdouble(3.941e-05, 3.333e-05, 0.0, -1.449e-05, -1.661e-05, 
        -1.424e-05, -1.183e-05, -6.842e-06, -4.915e-06, -3.411e-06, 
        0.0, 0.0, 3.333e-05, 2.862e-05, 0.0, 
        -1.244e-05, -1.431e-05, -1.233e-05, -1.032e-05, -5.883e-06, 
        -4.154e-06, -2.902e-06, -2.128e-06, 0.0, 0.0, 
        0.0, 0.0, 0.0, 0.0, 0.0, 
        0.0, 0.0, 0.0, 0.0, 0.0, 
        0.0, -1.449e-05, -1.244e-05, 0.0, 5.84e-06, 
        6.649e-06, 5.72e-06, 4.812e-06, 2.708e-06, 1.869e-06, 
        1.33e-06, 9.186e-07, 6.446e-07, -1.661e-05, -1.431e-05, 
        0.0, 6.649e-06, 7.966e-06, 6.898e-06, 5.794e-06, 
        3.157e-06, 2.184e-06, 1.567e-06, 1.084e-06, 7.575e-07, 
        -1.424e-05, -1.233e-05, 0.0, 5.72e-06, 6.898e-06, 
        6.341e-06, 5.347e-06, 2.859e-06, 1.991e-06, 1.431e-06, 
        9.839e-07, 6.886e-07, -1.183e-05, -1.032e-05, 0.0, 
        4.812e-06, 5.794e-06, 5.347e-06, 4.854e-06, 2.628e-06, 
        1.809e-06, 1.289e-06, 9.02e-07, 6.146e-07, -6.842e-06, 
        -5.883e-06, 0.0, 2.708e-06, 3.157e-06, 2.859e-06, 
        2.628e-06, 1.863e-06, 1.296e-06, 8.882e-07, 6.108e-07, 
        4.283e-07, -4.915e-06, -4.154e-06, 0.0, 1.869e-06, 
        2.184e-06, 1.991e-06, 1.809e-06, 1.296e-06, 1.217e-06, 
        8.669e-07, 5.751e-07, 3.882e-07, -3.411e-06, -2.902e-06, 
        0.0, 1.33e-06, 1.567e-06, 1.431e-06, 1.289e-06, 
        8.882e-07, 8.669e-07, 9.522e-07, 6.717e-07, 4.293e-07, 
        0.0, -2.128e-06, 0.0, 9.186e-07, 1.084e-06, 
        9.839e-07, 9.02e-07, 6.108e-07, 5.751e-07, 6.717e-07, 
        7.911e-07, 5.493e-07, 0.0, 0.0, 0.0, 
        6.446e-07, 7.575e-07, 6.886e-07, 6.146e-07, 4.283e-07, 
        3.882e-07, 4.293e-07, 5.493e-07, 7.027e-07)
)

process.ecal_pulse_shape_parameters = cms.PSet(
    EBCorrNoiseMatrixG01 = cms.vdouble(1.0, 0.73354, 0.64442, 0.58851, 0.55425, 
        0.53082, 0.51916, 0.51097, 0.50732, 0.50409),
    EBCorrNoiseMatrixG06 = cms.vdouble(1.0, 0.70946, 0.58021, 0.49846, 0.45006, 
        0.41366, 0.39699, 0.38478, 0.37847, 0.37055),
    EBCorrNoiseMatrixG12 = cms.vdouble(1.0, 0.71073, 0.55721, 0.46089, 0.40449, 
        0.35931, 0.33924, 0.32439, 0.31581, 0.30481),
    EBPulseShapeCovariance = cms.vdouble(3.001e-06, 1.233e-05, 0.0, -4.416e-06, -4.571e-06, 
        -3.614e-06, -2.636e-06, -1.286e-06, -8.41e-07, -5.296e-07, 
        0.0, 0.0, 1.233e-05, 6.154e-05, 0.0, 
        -2.2e-05, -2.309e-05, -1.838e-05, -1.373e-05, -7.334e-06, 
        -5.088e-06, -3.745e-06, -2.428e-06, 0.0, 0.0, 
        0.0, 0.0, 0.0, 0.0, 0.0, 
        0.0, 0.0, 0.0, 0.0, 0.0, 
        0.0, -4.416e-06, -2.2e-05, 0.0, 8.319e-06, 
        8.545e-06, 6.792e-06, 5.059e-06, 2.678e-06, 1.816e-06, 
        1.223e-06, 8.245e-07, 5.589e-07, -4.571e-06, -2.309e-05, 
        0.0, 8.545e-06, 9.182e-06, 7.219e-06, 5.388e-06, 
        2.853e-06, 1.944e-06, 1.324e-06, 9.083e-07, 6.335e-07, 
        -3.614e-06, -1.838e-05, 0.0, 6.792e-06, 7.219e-06, 
        6.016e-06, 4.437e-06, 2.385e-06, 1.636e-06, 1.118e-06, 
        7.754e-07, 5.556e-07, -2.636e-06, -1.373e-05, 0.0, 
        5.059e-06, 5.388e-06, 4.437e-06, 3.602e-06, 1.917e-06, 
        1.322e-06, 9.079e-07, 6.529e-07, 4.752e-07, -1.286e-06, 
        -7.334e-06, 0.0, 2.678e-06, 2.853e-06, 2.385e-06, 
        1.917e-06, 1.375e-06, 9.1e-07, 6.455e-07, 4.693e-07, 
        3.657e-07, -8.41e-07, -5.088e-06, 0.0, 1.816e-06, 
        1.944e-06, 1.636e-06, 1.322e-06, 9.1e-07, 9.115e-07, 
        6.062e-07, 4.436e-07, 3.422e-07, -5.296e-07, -3.745e-06, 
        0.0, 1.223e-06, 1.324e-06, 1.118e-06, 9.079e-07, 
        6.455e-07, 6.062e-07, 7.217e-07, 4.862e-07, 3.768e-07, 
        0.0, -2.428e-06, 0.0, 8.245e-07, 9.083e-07, 
        7.754e-07, 6.529e-07, 4.693e-07, 4.436e-07, 4.862e-07, 
        6.509e-07, 4.418e-07, 0.0, 0.0, 0.0, 
        5.589e-07, 6.335e-07, 5.556e-07, 4.752e-07, 3.657e-07, 
        3.422e-07, 3.768e-07, 4.418e-07, 6.142e-07),
    EBPulseShapeTemplate = cms.vdouble(0.0113979, 0.758151, 1.0, 0.887744, 0.673548, 
        0.474332, 0.319561, 0.215144, 0.147464, 0.101087, 
        0.0693181, 0.0475044),
    EBdigiCollection = cms.string(''),
    EECorrNoiseMatrixG01 = cms.vdouble(1.0, 0.72698, 0.62048, 0.55691, 0.51848, 
        0.49147, 0.47813, 0.47007, 0.46621, 0.46265),
    EECorrNoiseMatrixG06 = cms.vdouble(1.0, 0.71217, 0.47464, 0.34056, 0.26282, 
        0.20287, 0.17734, 0.16256, 0.15618, 0.14443),
    EECorrNoiseMatrixG12 = cms.vdouble(1.0, 0.71373, 0.44825, 0.30152, 0.21609, 
        0.14786, 0.11772, 0.10165, 0.09465, 0.08098),
    EEPulseShapeCovariance = cms.vdouble(3.941e-05, 3.333e-05, 0.0, -1.449e-05, -1.661e-05, 
        -1.424e-05, -1.183e-05, -6.842e-06, -4.915e-06, -3.411e-06, 
        0.0, 0.0, 3.333e-05, 2.862e-05, 0.0, 
        -1.244e-05, -1.431e-05, -1.233e-05, -1.032e-05, -5.883e-06, 
        -4.154e-06, -2.902e-06, -2.128e-06, 0.0, 0.0, 
        0.0, 0.0, 0.0, 0.0, 0.0, 
        0.0, 0.0, 0.0, 0.0, 0.0, 
        0.0, -1.449e-05, -1.244e-05, 0.0, 5.84e-06, 
        6.649e-06, 5.72e-06, 4.812e-06, 2.708e-06, 1.869e-06, 
        1.33e-06, 9.186e-07, 6.446e-07, -1.661e-05, -1.431e-05, 
        0.0, 6.649e-06, 7.966e-06, 6.898e-06, 5.794e-06, 
        3.157e-06, 2.184e-06, 1.567e-06, 1.084e-06, 7.575e-07, 
        -1.424e-05, -1.233e-05, 0.0, 5.72e-06, 6.898e-06, 
        6.341e-06, 5.347e-06, 2.859e-06, 1.991e-06, 1.431e-06, 
        9.839e-07, 6.886e-07, -1.183e-05, -1.032e-05, 0.0, 
        4.812e-06, 5.794e-06, 5.347e-06, 4.854e-06, 2.628e-06, 
        1.809e-06, 1.289e-06, 9.02e-07, 6.146e-07, -6.842e-06, 
        -5.883e-06, 0.0, 2.708e-06, 3.157e-06, 2.859e-06, 
        2.628e-06, 1.863e-06, 1.296e-06, 8.882e-07, 6.108e-07, 
        4.283e-07, -4.915e-06, -4.154e-06, 0.0, 1.869e-06, 
        2.184e-06, 1.991e-06, 1.809e-06, 1.296e-06, 1.217e-06, 
        8.669e-07, 5.751e-07, 3.882e-07, -3.411e-06, -2.902e-06, 
        0.0, 1.33e-06, 1.567e-06, 1.431e-06, 1.289e-06, 
        8.882e-07, 8.669e-07, 9.522e-07, 6.717e-07, 4.293e-07, 
        0.0, -2.128e-06, 0.0, 9.186e-07, 1.084e-06, 
        9.839e-07, 9.02e-07, 6.108e-07, 5.751e-07, 6.717e-07, 
        7.911e-07, 5.493e-07, 0.0, 0.0, 0.0, 
        6.446e-07, 7.575e-07, 6.886e-07, 6.146e-07, 4.283e-07, 
        3.882e-07, 4.293e-07, 5.493e-07, 7.027e-07),
    EEPulseShapeTemplate = cms.vdouble(0.116442, 0.756246, 1.0, 0.897182, 0.686831, 
        0.491506, 0.344111, 0.245731, 0.174115, 0.123361, 
        0.0874288, 0.061957),
    EEdigiCollection = cms.string(''),
    ESdigiCollection = cms.string(''),
    EcalPreMixStage1 = cms.bool(False),
    EcalPreMixStage2 = cms.bool(False),
    UseLCcorrection = cms.untracked.bool(True)
)

process.ecal_pulse_shape_templates = cms.PSet(
    EBPulseShapeTemplate = cms.vdouble(0.0113979, 0.758151, 1.0, 0.887744, 0.673548, 
        0.474332, 0.319561, 0.215144, 0.147464, 0.101087, 
        0.0693181, 0.0475044),
    EEPulseShapeTemplate = cms.vdouble(0.116442, 0.756246, 1.0, 0.897182, 0.686831, 
        0.491506, 0.344111, 0.245731, 0.174115, 0.123361, 
        0.0874288, 0.061957)
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.modPSet = cms.PSet(
    electron_config = cms.PSet(
        WP70PU = cms.InputTag("eleSelectionProducers","WP70PU"),
        WP80PU = cms.InputTag("eleSelectionProducers","WP80PU"),
        WP90PU = cms.InputTag("eleSelectionProducers","WP90PU"),
        electronSrc = cms.InputTag("slimmedElectrons"),
        energySCEleMust = cms.InputTag("eleNewEnergiesProducer","energySCEleMust"),
        energySCEleMustVar = cms.InputTag("eleNewEnergiesProducer","energySCEleMustVar"),
        energySCElePho = cms.InputTag("eleNewEnergiesProducer","energySCElePho"),
        energySCElePhoVar = cms.InputTag("eleNewEnergiesProducer","energySCElePhoVar"),
        fiducial = cms.InputTag("eleSelectionProducers","fiducial"),
        loose = cms.InputTag("eleSelectionProducers","loose"),
        loose25nsRun2 = cms.InputTag("eleSelectionProducers","loose25nsRun2"),
        loose50nsRun2 = cms.InputTag("eleSelectionProducers","loose50nsRun2"),
        medium = cms.InputTag("eleSelectionProducers","medium"),
        medium25nsRun2 = cms.InputTag("eleSelectionProducers","medium25nsRun2"),
        medium50nsRun2 = cms.InputTag("eleSelectionProducers","medium50nsRun2"),
        tight = cms.InputTag("eleSelectionProducers","tight"),
        tight25nsRun2 = cms.InputTag("eleSelectionProducers","tight25nsRun2"),
        tight50nsRun2 = cms.InputTag("eleSelectionProducers","tight50nsRun2")
    ),
    modifierName = cms.string('EGExtraInfoModifierFromFloatValueMaps'),
    photon_config = cms.PSet(

    )
)

process.modPSetBis = cms.PSet(
    electron_config = cms.PSet(
        WP70PU = cms.InputTag("eleSelectionProducers","WP70PU"),
        WP80PU = cms.InputTag("eleSelectionProducers","WP80PU"),
        WP90PU = cms.InputTag("eleSelectionProducers","WP90PU"),
        electronSrc = cms.InputTag("slimmedElectrons"),
        energySCEleMust = cms.InputTag("eleNewEnergiesProducer","energySCEleMust"),
        energySCEleMustVar = cms.InputTag("eleNewEnergiesProducer","energySCEleMustVar"),
        energySCElePho = cms.InputTag("eleNewEnergiesProducer","energySCElePho"),
        energySCElePhoVar = cms.InputTag("eleNewEnergiesProducer","energySCElePhoVar"),
        fiducial = cms.InputTag("eleSelectionProducers","fiducial"),
        loose = cms.InputTag("eleSelectionProducers","loose"),
        loose25nsRun2 = cms.InputTag("eleSelectionProducers","loose25nsRun2"),
        loose50nsRun2 = cms.InputTag("eleSelectionProducers","loose50nsRun2"),
        medium = cms.InputTag("eleSelectionProducers","medium"),
        medium25nsRun2 = cms.InputTag("eleSelectionProducers","medium25nsRun2"),
        medium50nsRun2 = cms.InputTag("eleSelectionProducers","medium50nsRun2"),
        tight = cms.InputTag("eleSelectionProducers","tight"),
        tight25nsRun2 = cms.InputTag("eleSelectionProducers","tight25nsRun2"),
        tight50nsRun2 = cms.InputTag("eleSelectionProducers","tight50nsRun2")
    ),
    modifierName = cms.string('EleIDModifierFromValueMaps'),
    photon_config = cms.PSet(

    )
)

process.mvaEleID_PHYS14_PU20bx25_nonTrig_V1_producer_config = cms.PSet(
    mvaName = cms.string('ElectronMVAEstimatorRun2Phys14NonTrig'),
    mvaTag = cms.string('25nsV1'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_10_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_10_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_10_oldscenario2phys14_BDT.weights.xml')
)

process.mvaEleID_PHYS14_PU20bx25_nonTrig_V1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Phys14NonTrig25nsV1Categories"),
        mvaCuts = cms.vdouble(-0.253, 0.081, -0.081, 0.965, 0.917, 
            0.683),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Phys14NonTrig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-PHYS14-PU20bx25-nonTrig-V1-wp80'),
    isPOGApproved = cms.untracked.bool(False)
)

process.mvaEleID_PHYS14_PU20bx25_nonTrig_V1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Phys14NonTrig25nsV1Categories"),
        mvaCuts = cms.vdouble(-0.483, -0.267, -0.323, 0.933, 0.825, 
            0.337),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Phys14NonTrig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-PHYS14-PU20bx25-nonTrig-V1-wp90'),
    isPOGApproved = cms.untracked.bool(False)
)

process.mvaEleID_Spring15_25ns_Trig_V1_producer_config = cms.PSet(
    beamSpot = cms.InputTag("offlineBeamSpot"),
    conversionsAOD = cms.InputTag("allConversions"),
    conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
    mvaName = cms.string('ElectronMVAEstimatorRun2Spring15Trig'),
    mvaTag = cms.string('25nsV1'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml')
)

process.mvaEleID_Spring15_25ns_Trig_V1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Categories"),
        mvaCuts = cms.vdouble(0.988153, 0.96791, 0.841729),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-25ns-Trig-V1-wp80'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaEleID_Spring15_25ns_Trig_V1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Categories"),
        mvaCuts = cms.vdouble(0.972153, 0.922126, 0.610764),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-25ns-Trig-V1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaEleID_Spring15_25ns_nonTrig_V1_producer_config = cms.PSet(
    beamSpot = cms.InputTag("offlineBeamSpot"),
    conversionsAOD = cms.InputTag("allConversions"),
    conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
    mvaName = cms.string('ElectronMVAEstimatorRun2Spring15NonTrig'),
    mvaTag = cms.string('25nsV1'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml')
)

process.mvaEleID_Spring15_25ns_nonTrig_V1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories"),
        mvaCuts = cms.vdouble(0.287435, 0.221846, -0.303263, 0.967083, 0.929117, 
            0.726311),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-25ns-nonTrig-V1-wp80'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaEleID_Spring15_25ns_nonTrig_V1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories"),
        mvaCuts = cms.vdouble(-0.083313, -0.235222, -0.67099, 0.913286, 0.805013, 
            0.358969),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-25ns-nonTrig-V1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaEleID_Spring15_25ns_nonTrig_V1_wpLoose = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories"),
        mvaCuts = cms.vdouble(-0.265, -0.556, -0.551, -0.072, -0.286, 
            -0.267),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-25ns-nonTrig-V1-wpLoose'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaEleID_Spring15_50ns_Trig_V1_producer_config = cms.PSet(
    beamSpot = cms.InputTag("offlineBeamSpot"),
    conversionsAOD = cms.InputTag("allConversions"),
    conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
    mvaName = cms.string('ElectronMVAEstimatorRun2Spring15Trig'),
    mvaTag = cms.string('50nsV1'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml')
)

process.mvaEleID_Spring15_50ns_Trig_V1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig50nsV1Categories"),
        mvaCuts = cms.vdouble(0.981841, 0.946762, 0.79704),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig50nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-50ns-Trig-V1-wp80'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaEleID_Spring15_50ns_Trig_V1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig50nsV1Categories"),
        mvaCuts = cms.vdouble(0.953843, 0.849994, 0.514118),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig50nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-50ns-Trig-V1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaPhoID_PHYS14_PU20bx25_nonTrig_V1_producer_config = cms.PSet(
    esEffSigmaRRMap = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
    full5x5E1x3Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E1x3"),
    full5x5E2x2Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x2"),
    full5x5E2x5MaxMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x5Max"),
    full5x5E5x5Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E5x5"),
    full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
    full5x5SigmaIEtaIPhiMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
    mvaName = cms.string('PhotonMVAEstimatorRun2Phys14NonTrig'),
    mvaTag = cms.string('25nsV1'),
    phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
    phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
    phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    useValueMaps = cms.bool(True),
    weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/PHYS14/photon_general_MVA_phys14_pu20bx25_EB_V1.weights.xml', 
        'RecoEgamma/PhotonIdentification/data/PHYS14/photon_general_MVA_phys14_pu20bx25_EE_V1.weights.xml')
)

process.mvaPhoID_PHYS14_PU20bx25_nonTrig_V1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Phys14NonTrig25nsV1Categories"),
        mvaCuts = cms.vdouble(0.593, 0.679),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Phys14NonTrig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-PHYS14-PU20bx25-nonTrig-V1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaPhoID_Spring15_25ns_nonTrig_V2_producer_config = cms.PSet(
    esEffSigmaRRMap = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
    full5x5E1x3Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E1x3"),
    full5x5E2x2Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x2"),
    full5x5E2x5MaxMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x5Max"),
    full5x5E5x5Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E5x5"),
    full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
    full5x5SigmaIEtaIPhiMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
    mvaName = cms.string('PhotonMVAEstimatorRun2Spring15NonTrig'),
    mvaTag = cms.string('25nsV2'),
    phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
    phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
    phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    useValueMaps = cms.bool(True),
    weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_25ns_EB_V2.weights.xml', 
        'RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_25ns_EE_V2.weights.xml')
)

process.mvaPhoID_Spring15_25ns_nonTrig_V2_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig25nsV2Categories"),
        mvaCuts = cms.vdouble(0.374, 0.336),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig25nsV2Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-Spring15-25ns-nonTrig-V2-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaPhoID_Spring15_25ns_nonTrig_V2p1_producer_config = cms.PSet(
    esEffSigmaRRMap = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
    full5x5E1x3Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E1x3"),
    full5x5E2x2Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x2"),
    full5x5E2x5MaxMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x5Max"),
    full5x5E5x5Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E5x5"),
    full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
    full5x5SigmaIEtaIPhiMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
    mvaName = cms.string('PhotonMVAEstimatorRun2Spring15NonTrig'),
    mvaTag = cms.string('25nsV2p1'),
    phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
    phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
    phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    useValueMaps = cms.bool(False),
    weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_25ns_EB_V2.weights.xml', 
        'RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_25ns_EE_V2.weights.xml')
)

process.mvaPhoID_Spring15_25ns_nonTrig_V2p1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig25nsV2p1Categories"),
        mvaCuts = cms.vdouble(0.374, 0.336),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig25nsV2p1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-Spring15-25ns-nonTrig-V2p1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaPhoID_Spring15_50ns_nonTrig_V1_producer_config = cms.PSet(
    esEffSigmaRRMap = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
    full5x5E1x3Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E1x3"),
    full5x5E2x2Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x2"),
    full5x5E2x5MaxMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x5Max"),
    full5x5E5x5Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E5x5"),
    full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
    full5x5SigmaIEtaIPhiMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
    mvaName = cms.string('PhotonMVAEstimatorRun2Spring15NonTrig'),
    mvaTag = cms.string('50nsV1'),
    phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
    phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
    phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    useValueMaps = cms.bool(True),
    weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_50ns_EB_V1.weights.xml', 
        'RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_50ns_EE_V1.weights.xml')
)

process.mvaPhoID_Spring15_50ns_nonTrig_V1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig50nsV1Categories"),
        mvaCuts = cms.vdouble(0.284, 0.432),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig50nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-Spring15-50ns-nonTrig-V1-wp90'),
    isPOGApproved = cms.untracked.bool(False)
)

process.mvaPhoID_Spring15_50ns_nonTrig_V2_producer_config = cms.PSet(
    esEffSigmaRRMap = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
    full5x5E1x3Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E1x3"),
    full5x5E2x2Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x2"),
    full5x5E2x5MaxMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x5Max"),
    full5x5E5x5Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E5x5"),
    full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
    full5x5SigmaIEtaIPhiMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
    mvaName = cms.string('PhotonMVAEstimatorRun2Spring15NonTrig'),
    mvaTag = cms.string('50nsV2'),
    phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
    phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
    phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    useValueMaps = cms.bool(True),
    weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_50ns_EB_V2.weights.xml', 
        'RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_50ns_EE_V2.weights.xml')
)

process.mvaPhoID_Spring15_50ns_nonTrig_V2_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig50nsV2Categories"),
        mvaCuts = cms.vdouble(0.29538, 0.45837),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig50nsV2Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-Spring15-50ns-nonTrig-V2-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaPhoID_Spring15_50ns_nonTrig_V2p1_producer_config = cms.PSet(
    esEffSigmaRRMap = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
    full5x5E1x3Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E1x3"),
    full5x5E2x2Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x2"),
    full5x5E2x5MaxMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x5Max"),
    full5x5E5x5Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E5x5"),
    full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
    full5x5SigmaIEtaIPhiMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
    mvaName = cms.string('PhotonMVAEstimatorRun2Spring15NonTrig'),
    mvaTag = cms.string('50nsV2p1'),
    phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
    phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
    phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    useValueMaps = cms.bool(False),
    weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_50ns_EB_V2.weights.xml', 
        'RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_50ns_EE_V2.weights.xml')
)

process.mvaPhoID_Spring15_50ns_nonTrig_V2p1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig50nsV2p1Categories"),
        mvaCuts = cms.vdouble(0.29538, 0.45837),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig50nsV2p1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-Spring15-50ns-nonTrig-V2p1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.egamma_modifications = cms.VPSet()

process.mvaConfigsForEleProducer = cms.VPSet(cms.PSet(
    mvaName = cms.string('ElectronMVAEstimatorRun2Phys14NonTrig'),
    mvaTag = cms.string('25nsV1'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_10_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_10_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_10_oldscenario2phys14_BDT.weights.xml')
), 
    cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        conversionsAOD = cms.InputTag("allConversions"),
        conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
        mvaName = cms.string('ElectronMVAEstimatorRun2Spring15NonTrig'),
        mvaTag = cms.string('25nsV1'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml')
    ), 
    cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        conversionsAOD = cms.InputTag("allConversions"),
        conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
        mvaName = cms.string('ElectronMVAEstimatorRun2Spring15Trig'),
        mvaTag = cms.string('50nsV1'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml')
    ), 
    cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        conversionsAOD = cms.InputTag("allConversions"),
        conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
        mvaName = cms.string('ElectronMVAEstimatorRun2Spring15Trig'),
        mvaTag = cms.string('25nsV1'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml')
    ))

process.mvaConfigsForPhoProducer = cms.VPSet(cms.PSet(
    esEffSigmaRRMap = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
    full5x5E1x3Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E1x3"),
    full5x5E2x2Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x2"),
    full5x5E2x5MaxMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x5Max"),
    full5x5E5x5Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E5x5"),
    full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
    full5x5SigmaIEtaIPhiMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
    mvaName = cms.string('PhotonMVAEstimatorRun2Phys14NonTrig'),
    mvaTag = cms.string('25nsV1'),
    phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
    phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
    phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    useValueMaps = cms.bool(True),
    weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/PHYS14/photon_general_MVA_phys14_pu20bx25_EB_V1.weights.xml', 
        'RecoEgamma/PhotonIdentification/data/PHYS14/photon_general_MVA_phys14_pu20bx25_EE_V1.weights.xml')
), 
    cms.PSet(
        esEffSigmaRRMap = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
        full5x5E1x3Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E1x3"),
        full5x5E2x2Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x2"),
        full5x5E2x5MaxMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x5Max"),
        full5x5E5x5Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E5x5"),
        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
        full5x5SigmaIEtaIPhiMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
        mvaName = cms.string('PhotonMVAEstimatorRun2Spring15NonTrig'),
        mvaTag = cms.string('50nsV1'),
        phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
        phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
        phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
        rho = cms.InputTag("fixedGridRhoFastjetAll"),
        useValueMaps = cms.bool(True),
        weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_50ns_EB_V1.weights.xml', 
            'RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_50ns_EE_V1.weights.xml')
    ), 
    cms.PSet(
        esEffSigmaRRMap = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
        full5x5E1x3Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E1x3"),
        full5x5E2x2Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x2"),
        full5x5E2x5MaxMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x5Max"),
        full5x5E5x5Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E5x5"),
        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
        full5x5SigmaIEtaIPhiMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
        mvaName = cms.string('PhotonMVAEstimatorRun2Spring15NonTrig'),
        mvaTag = cms.string('50nsV2'),
        phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
        phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
        phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
        rho = cms.InputTag("fixedGridRhoFastjetAll"),
        useValueMaps = cms.bool(True),
        weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_50ns_EB_V2.weights.xml', 
            'RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_50ns_EE_V2.weights.xml')
    ), 
    cms.PSet(
        esEffSigmaRRMap = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
        full5x5E1x3Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E1x3"),
        full5x5E2x2Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x2"),
        full5x5E2x5MaxMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x5Max"),
        full5x5E5x5Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E5x5"),
        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
        full5x5SigmaIEtaIPhiMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
        mvaName = cms.string('PhotonMVAEstimatorRun2Spring15NonTrig'),
        mvaTag = cms.string('25nsV2'),
        phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
        phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
        phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
        rho = cms.InputTag("fixedGridRhoFastjetAll"),
        useValueMaps = cms.bool(True),
        weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_25ns_EB_V2.weights.xml', 
            'RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_25ns_EE_V2.weights.xml')
    ), 
    cms.PSet(
        esEffSigmaRRMap = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
        full5x5E1x3Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E1x3"),
        full5x5E2x2Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x2"),
        full5x5E2x5MaxMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x5Max"),
        full5x5E5x5Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E5x5"),
        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
        full5x5SigmaIEtaIPhiMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
        mvaName = cms.string('PhotonMVAEstimatorRun2Spring15NonTrig'),
        mvaTag = cms.string('50nsV2p1'),
        phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
        phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
        phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
        rho = cms.InputTag("fixedGridRhoFastjetAll"),
        useValueMaps = cms.bool(False),
        weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_50ns_EB_V2.weights.xml', 
            'RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_50ns_EE_V2.weights.xml')
    ), 
    cms.PSet(
        esEffSigmaRRMap = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
        full5x5E1x3Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E1x3"),
        full5x5E2x2Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x2"),
        full5x5E2x5MaxMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x5Max"),
        full5x5E5x5Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E5x5"),
        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
        full5x5SigmaIEtaIPhiMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
        mvaName = cms.string('PhotonMVAEstimatorRun2Spring15NonTrig'),
        mvaTag = cms.string('25nsV2p1'),
        phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
        phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
        phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
        rho = cms.InputTag("fixedGridRhoFastjetAll"),
        useValueMaps = cms.bool(False),
        weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_25ns_EB_V2.weights.xml', 
            'RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_25ns_EE_V2.weights.xml')
    ))

process.EleSCSelector = cms.EDProducer("CandViewShallowCloneCombiner",
    checkCharge = cms.bool(False),
    cut = cms.string('40 < mass < 140'),
    decay = cms.string('PassingVetoId eleSC')
)


process.GsfMatchedPhotonCands = cms.EDProducer("ElectronMatchedCandidateProducer",
    ReferenceElectronCollection = cms.untracked.InputTag("goodElectrons"),
    deltaR = cms.untracked.double(0.3),
    src = cms.InputTag("goodPhotons")
)


process.PatElectronTriggerMatchHLTEle_Ele20SC4Mass50v7 = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('path( "HLT_Ele20_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC4_Mass50_v7" )'),
    maxDPtRel = cms.double(0.5),
    maxDeltaR = cms.double(0.5),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("patElectrons")
)


process.PatElectronsTriggerMatch = cms.EDProducer("PATTriggerMatchElectronEmbedder",
    matches = cms.VInputTag("PatElectronTriggerMatchHLTEle_Ele20SC4Mass50v7"),
    src = cms.InputTag("PatElectrons")
)


process.WZSelector = cms.EDProducer("CandViewMerger",
    src = cms.VInputTag("WenuSelector", "ZeeSelector", "EleSCSelector")
)


process.WenuSelector = cms.EDProducer("CandViewShallowCloneCombiner",
    checkCharge = cms.bool(False),
    cut = cms.string('daughter(0).pt > 25.000000 && daughter(1).pt > 30.000000 && sqrt(2*daughter(0).pt*daughter(1).pt*(1 - cos(daughter(0).phi - daughter(1).phi))) > 50.000000'),
    decay = cms.string('pfMet PassingVetoId')
)


process.ZeeSelector = cms.EDProducer("CandViewShallowCloneCombiner",
    checkCharge = cms.bool(False),
    cut = cms.string('40 < mass < 140'),
    decay = cms.string('PassingVetoId PassingVetoId')
)


process.ZmmgCandidates = cms.EDProducer("CandViewShallowCloneCombiner",
    checkCharge = cms.bool(False),
    cut = cms.string('\n        daughter(0).daughter(1).pt + daughter(1).pt > 20 &\n        min(deltaR(daughter(0).daughter(0).eta,\n                   daughter(0).daughter(0).phi,\n                   daughter(1).eta,\n                   daughter(1).phi),\n            deltaR(daughter(0).daughter(1).eta,\n                   daughter(0).daughter(1).phi,\n                   daughter(1).eta,\n                   daughter(1).phi)) < 1.5 &\n        mass + daughter(0).mass < 200 &\n        mass > 40\n        '),
    decay = cms.string('ZmmgDimuons ZmmgPhotons')
)


process.ZmmgDimuons = cms.EDProducer("CandViewShallowCloneCombiner",
    checkCharge = cms.bool(True),
    cut = cms.string('mass > 30'),
    decay = cms.string('ZmmgLeadingMuons@+ ZmmgTrailingMuons@-')
)


process.ZmmgMergedSuperClusters = cms.EDProducer("EgammaSuperClusterMerger",
    src = cms.VInputTag(cms.InputTag("correctedHybridSuperClusters"), cms.InputTag("correctedMulti5x5SuperClustersWithPreshower"))
)


process.ZmmgPhotonCandidates = cms.EDProducer("ConcreteEcalCandidateProducer",
    particleType = cms.string('gamma'),
    src = cms.InputTag("ZmmgMergedSuperClusters")
)


process.alCaIsolatedElectrons = cms.EDProducer("AlCaECALRecHitReducer",
    EESuperClusterCollection = cms.InputTag("correctedMulti5x5SuperClustersWithPreshower"),
    alcaBarrelHitCollection = cms.string('alcaBarrelHits'),
    alcaCaloClusterCollection = cms.string('alcaCaloCluster'),
    alcaEndcapHitCollection = cms.string('alcaEndcapHits'),
    ebRecHitsLabel = cms.InputTag("reducedEcalRecHitsEB"),
    eeRecHitsLabel = cms.InputTag("reducedEcalRecHitsEE"),
    electronLabel = cms.InputTag("gedGsfElectrons"),
    etaSize = cms.int32(15),
    minEta_highEtaSC = cms.double(2.4),
    phiSize = cms.int32(61),
    photonLabel = cms.InputTag("gedPhotons"),
    srcLabels = cms.VInputTag("gedGsfElectrons")
)


process.alcaElectronTracksReducer = cms.EDProducer("AlCaElectronTracksReducer",
    alcaTrackCollection = cms.string('alCaElectronTracks'),
    alcaTrackExtraCollection = cms.string('alCaElectronTracksExtra'),
    electronLabel = cms.InputTag("slimmedElectrons"),
    generalTracksExtraLabel = cms.InputTag("generalTracksExtra"),
    generalTracksLabel = cms.InputTag("generalTracks")
)


process.bunchSpacingProducer = cms.EDProducer("BunchSpacingProducer")


process.castorDigis = cms.EDProducer("CastorRawToDigi",
    CastorCtdc = cms.bool(False),
    CastorFirstFED = cms.int32(690),
    ComplainEmptyData = cms.untracked.bool(False),
    ExceptionEmptyData = cms.untracked.bool(False),
    ExpectedOrbitMessageTime = cms.int32(-1),
    FEDs = cms.untracked.vint32(690, 691, 692),
    FilterDataQuality = cms.bool(True),
    InputLabel = cms.InputTag("rawDataCollector"),
    UnpackTTP = cms.bool(True),
    UseNominalOrbitMessageTime = cms.bool(True),
    firstSample = cms.int32(0),
    lastSample = cms.int32(9),
    silent = cms.untracked.bool(False)
)


process.cleanedHybridSuperClusters = cms.EDProducer("HybridClusterProducer",
    HybridBarrelSeedThr = cms.double(1.0),
    RecHitFlagToBeExcluded = cms.vstring('kFaultyHardware', 
        'kTowerRecovered', 
        'kDead'),
    RecHitSeverityToBeExcluded = cms.vstring('kWeird', 
        'kBad', 
        'kTime'),
    basicclusterCollection = cms.string('hybridBarrelBasicClusters'),
    clustershapecollection = cms.string(''),
    dynamicEThresh = cms.bool(False),
    dynamicPhiRoad = cms.bool(False),
    eThreshA = cms.double(0.003),
    eThreshB = cms.double(0.1),
    eseed = cms.double(0.35),
    ethresh = cms.double(0.1),
    ewing = cms.double(0.0),
    excludeFlagged = cms.bool(True),
    posCalcParameters = cms.PSet(
        LogWeighted = cms.bool(True),
        T0_barl = cms.double(7.4),
        T0_endc = cms.double(3.1),
        T0_endcPresh = cms.double(1.2),
        W0 = cms.double(4.2),
        X0 = cms.double(0.89)
    ),
    recHitsCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    shapeAssociation = cms.string('hybridShapeAssoc'),
    step = cms.int32(17),
    superclusterCollection = cms.string(''),
    useEtForXi = cms.bool(True),
    xi = cms.double(0.0)
)


process.combW = cms.EDProducer("CandViewShallowCloneCombiner",
    checkCharge = cms.bool(False),
    cut = cms.string(''),
    decay = cms.string('genEleFromW genNuFromW')
)


process.combZ = cms.EDProducer("CandViewShallowCloneCombiner",
    checkCharge = cms.bool(False),
    cut = cms.string('40 < mass < 140'),
    decay = cms.string('genEleFromZ genEleFromZ')
)


process.correctedHybridSuperClusters = cms.EDProducer("EgammaSCCorrectionMaker",
    applyCrackCorrection = cms.bool(True),
    applyEnergyCorrection = cms.bool(True),
    applyLocalContCorrection = cms.bool(True),
    corectedSuperClusterCollection = cms.string(''),
    crackCorrectorName = cms.string('EcalClusterCrackCorrection'),
    energyCorrectorName = cms.string('EcalClusterEnergyCorrectionObjectSpecific'),
    etThresh = cms.double(0.0),
    hyb_fCorrPset = cms.PSet(
        brLinearHighThr = cms.double(8.0),
        brLinearLowThr = cms.double(1.1),
        fBremVec = cms.vdouble(-0.04382, 0.1169, 0.9267, -0.0009413, 1.419),
        fEtEtaVec = cms.vdouble(0, 1.00121, -0.63672, 0, 0, 
            0, 0.5655, 6.457, 0.5081, 8.0, 
            1.023, -0.00181)
    ),
    localContCorrectorName = cms.string('EcalBasicClusterLocalContCorrection'),
    modeEB = cms.int32(0),
    modeEE = cms.int32(0),
    rawSuperClusterProducer = cms.InputTag("hybridSuperClusters"),
    recHitProducer = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    sigmaElectronicNoise = cms.double(0.03),
    superClusterAlgo = cms.string('Hybrid')
)


process.correctedMulti5x5SuperClustersWithPreshower = cms.EDProducer("EgammaSCCorrectionMaker",
    VerbosityLevel = cms.string('ERROR'),
    applyCrackCorrection = cms.bool(True),
    applyEnergyCorrection = cms.bool(True),
    applyLocalContCorrection = cms.bool(False),
    corectedSuperClusterCollection = cms.string(''),
    crackCorrectorName = cms.string('EcalClusterCrackCorrection'),
    energyCorrectorName = cms.string('EcalClusterEnergyCorrectionObjectSpecific'),
    etThresh = cms.double(0.0),
    fix_fCorrPset = cms.PSet(
        brLinearHighThr = cms.double(6.0),
        brLinearLowThr = cms.double(0.9),
        fBremVec = cms.vdouble(-0.05228, 0.08738, 0.9508, 0.002677, 1.221),
        fEtEtaVec = cms.vdouble(1, -0.4386, -32.38, 0.6372, 15.67, 
            -0.0928, -2.462, 1.138, 20.93)
    ),
    localContCorrectorName = cms.string('EcalBasicClusterLocalContCorrection'),
    modeEB = cms.int32(0),
    modeEE = cms.int32(0),
    rawSuperClusterProducer = cms.InputTag("multi5x5SuperClustersWithPreshower"),
    recHitProducer = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    sigmaElectronicNoise = cms.double(0.15),
    superClusterAlgo = cms.string('Multi5x5')
)


process.csctfDigis = cms.EDProducer("CSCTFUnpacker",
    MaxBX = cms.int32(9),
    MinBX = cms.int32(3),
    mappingFile = cms.string(''),
    producer = cms.InputTag("rawDataCollector"),
    slot2sector = cms.vint32(0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0),
    swapME1strips = cms.bool(False)
)


process.dttfDigis = cms.EDProducer("DTTFFEDReader",
    DTTF_FED_Source = cms.InputTag("rawDataCollector"),
    verbose = cms.untracked.bool(False)
)


process.ecalCompactTrigPrim = cms.EDProducer("EcalCompactTrigPrimProducer",
    inColl = cms.InputTag("ecalDigis","EcalTriggerPrimitives"),
    outColl = cms.string('')
)


process.ecalDetIdToBeRecovered = cms.EDProducer("EcalDetIdToBeRecoveredProducer",
    ebDetIdToBeRecovered = cms.string('ebDetId'),
    ebFEToBeRecovered = cms.string('ebFE'),
    ebIntegrityChIdErrors = cms.InputTag("ecalDigis","EcalIntegrityChIdErrors"),
    ebIntegrityGainErrors = cms.InputTag("ecalDigis","EcalIntegrityGainErrors"),
    ebIntegrityGainSwitchErrors = cms.InputTag("ecalDigis","EcalIntegrityGainSwitchErrors"),
    ebSrFlagCollection = cms.InputTag("ecalDigis"),
    eeDetIdToBeRecovered = cms.string('eeDetId'),
    eeFEToBeRecovered = cms.string('eeFE'),
    eeIntegrityChIdErrors = cms.InputTag("ecalDigis","EcalIntegrityChIdErrors"),
    eeIntegrityGainErrors = cms.InputTag("ecalDigis","EcalIntegrityGainErrors"),
    eeIntegrityGainSwitchErrors = cms.InputTag("ecalDigis","EcalIntegrityGainSwitchErrors"),
    eeSrFlagCollection = cms.InputTag("ecalDigis"),
    integrityBlockSizeErrors = cms.InputTag("ecalDigis","EcalIntegrityBlockSizeErrors"),
    integrityTTIdErrors = cms.InputTag("ecalDigis","EcalIntegrityTTIdErrors")
)


process.ecalDigis = cms.EDProducer("EcalRawToDigi",
    DoRegional = cms.bool(False),
    FEDs = cms.vint32(601, 602, 603, 604, 605, 
        606, 607, 608, 609, 610, 
        611, 612, 613, 614, 615, 
        616, 617, 618, 619, 620, 
        621, 622, 623, 624, 625, 
        626, 627, 628, 629, 630, 
        631, 632, 633, 634, 635, 
        636, 637, 638, 639, 640, 
        641, 642, 643, 644, 645, 
        646, 647, 648, 649, 650, 
        651, 652, 653, 654),
    FedLabel = cms.InputTag("listfeds"),
    InputLabel = cms.InputTag("rawDataCollector"),
    eventPut = cms.bool(True),
    feIdCheck = cms.bool(True),
    feUnpacking = cms.bool(True),
    forceToKeepFRData = cms.bool(False),
    headerUnpacking = cms.bool(True),
    memUnpacking = cms.bool(True),
    numbTriggerTSamples = cms.int32(1),
    numbXtalTSamples = cms.int32(10),
    orderedDCCIdList = cms.vint32(1, 2, 3, 4, 5, 
        6, 7, 8, 9, 10, 
        11, 12, 13, 14, 15, 
        16, 17, 18, 19, 20, 
        21, 22, 23, 24, 25, 
        26, 27, 28, 29, 30, 
        31, 32, 33, 34, 35, 
        36, 37, 38, 39, 40, 
        41, 42, 43, 44, 45, 
        46, 47, 48, 49, 50, 
        51, 52, 53, 54),
    orderedFedList = cms.vint32(601, 602, 603, 604, 605, 
        606, 607, 608, 609, 610, 
        611, 612, 613, 614, 615, 
        616, 617, 618, 619, 620, 
        621, 622, 623, 624, 625, 
        626, 627, 628, 629, 630, 
        631, 632, 633, 634, 635, 
        636, 637, 638, 639, 640, 
        641, 642, 643, 644, 645, 
        646, 647, 648, 649, 650, 
        651, 652, 653, 654),
    silentMode = cms.untracked.bool(True),
    srpUnpacking = cms.bool(True),
    syncCheck = cms.bool(True),
    tccUnpacking = cms.bool(True)
)


process.ecalGlobalUncalibRecHit = cms.EDProducer("EcalUncalibRecHitProducer",
    EBdigiCollection = cms.InputTag("ecalDigis","ebDigis"),
    EBhitCollection = cms.string('EcalUncalibRecHitsEB'),
    EEdigiCollection = cms.InputTag("ecalDigis","eeDigis"),
    EEhitCollection = cms.string('EcalUncalibRecHitsEE'),
    algo = cms.string('EcalUncalibRecHitWorkerGlobal'),
    algoPSet = cms.PSet(
        EBamplitudeFitParameters = cms.vdouble(1.138, 1.652),
        EBchi2Parameters = cms.vdouble(2.122, 0.022, 2.122, 0.022),
        EBtimeConstantTerm = cms.double(0.6),
        EBtimeFitLimits_Lower = cms.double(0.2),
        EBtimeFitLimits_Upper = cms.double(1.4),
        EBtimeFitParameters = cms.vdouble(-2.015452, 3.130702, -12.3473, 41.88921, -82.83944, 
            91.01147, -50.35761, 11.05621),
        EBtimeNconst = cms.double(28.5),
        EEamplitudeFitParameters = cms.vdouble(1.89, 1.4),
        EEchi2Parameters = cms.vdouble(2.122, 0.022, 2.122, 0.022),
        EEtimeConstantTerm = cms.double(1.0),
        EEtimeFitLimits_Lower = cms.double(0.2),
        EEtimeFitLimits_Upper = cms.double(1.4),
        EEtimeFitParameters = cms.vdouble(-2.390548, 3.553628, -17.62341, 67.67538, -133.213, 
            140.7432, -75.41106, 16.20277),
        EEtimeNconst = cms.double(31.8),
        amplitudeThresholdEB = cms.double(10),
        amplitudeThresholdEE = cms.double(10),
        chi2ThreshEB_ = cms.double(36.0),
        chi2ThreshEE_ = cms.double(95.0),
        ebPulseShape = cms.vdouble(5.2e-05, -5.26e-05, 6.66e-05, 0.1168, 0.7575, 
            1.0, 0.8876, 0.6732, 0.4741, 0.3194),
        ebSpikeThreshold = cms.double(1.042),
        eePulseShape = cms.vdouble(5.2e-05, -5.26e-05, 6.66e-05, 0.1168, 0.7575, 
            1.0, 0.8876, 0.6732, 0.4741, 0.3194),
        kPoorRecoFlagEB = cms.bool(True),
        kPoorRecoFlagEE = cms.bool(False),
        outOfTimeThresholdGain12mEB = cms.double(5),
        outOfTimeThresholdGain12mEE = cms.double(1000),
        outOfTimeThresholdGain12pEB = cms.double(5),
        outOfTimeThresholdGain12pEE = cms.double(1000),
        outOfTimeThresholdGain61mEB = cms.double(5),
        outOfTimeThresholdGain61mEE = cms.double(1000),
        outOfTimeThresholdGain61pEB = cms.double(5),
        outOfTimeThresholdGain61pEE = cms.double(1000)
    )
)


process.ecalMultiFitUncalibRecHit = cms.EDProducer("EcalUncalibRecHitProducer",
    EBdigiCollection = cms.InputTag("ecalDigis","ebDigis"),
    EBhitCollection = cms.string('EcalUncalibRecHitsEB'),
    EEdigiCollection = cms.InputTag("ecalDigis","eeDigis"),
    EEhitCollection = cms.string('EcalUncalibRecHitsEE'),
    algo = cms.string('EcalUncalibRecHitWorkerMultiFit'),
    algoPSet = cms.PSet(
        EBamplitudeFitParameters = cms.vdouble(1.138, 1.652),
        EBtimeConstantTerm = cms.double(0.6),
        EBtimeFitLimits_Lower = cms.double(0.2),
        EBtimeFitLimits_Upper = cms.double(1.4),
        EBtimeFitParameters = cms.vdouble(-2.015452, 3.130702, -12.3473, 41.88921, -82.83944, 
            91.01147, -50.35761, 11.05621),
        EBtimeNconst = cms.double(28.5),
        EEamplitudeFitParameters = cms.vdouble(1.89, 1.4),
        EEtimeConstantTerm = cms.double(1.0),
        EEtimeFitLimits_Lower = cms.double(0.2),
        EEtimeFitLimits_Upper = cms.double(1.4),
        EEtimeFitParameters = cms.vdouble(-2.390548, 3.553628, -17.62341, 67.67538, -133.213, 
            140.7432, -75.41106, 16.20277),
        EEtimeNconst = cms.double(31.8),
        EcalPulseShapeParameters = cms.PSet(
            EBCorrNoiseMatrixG01 = cms.vdouble(1.0, 0.73354, 0.64442, 0.58851, 0.55425, 
                0.53082, 0.51916, 0.51097, 0.50732, 0.50409),
            EBCorrNoiseMatrixG06 = cms.vdouble(1.0, 0.70946, 0.58021, 0.49846, 0.45006, 
                0.41366, 0.39699, 0.38478, 0.37847, 0.37055),
            EBCorrNoiseMatrixG12 = cms.vdouble(1.0, 0.71073, 0.55721, 0.46089, 0.40449, 
                0.35931, 0.33924, 0.32439, 0.31581, 0.30481),
            EBPulseShapeCovariance = cms.vdouble(3.001e-06, 1.233e-05, 0.0, -4.416e-06, -4.571e-06, 
                -3.614e-06, -2.636e-06, -1.286e-06, -8.41e-07, -5.296e-07, 
                0.0, 0.0, 1.233e-05, 6.154e-05, 0.0, 
                -2.2e-05, -2.309e-05, -1.838e-05, -1.373e-05, -7.334e-06, 
                -5.088e-06, -3.745e-06, -2.428e-06, 0.0, 0.0, 
                0.0, 0.0, 0.0, 0.0, 0.0, 
                0.0, 0.0, 0.0, 0.0, 0.0, 
                0.0, -4.416e-06, -2.2e-05, 0.0, 8.319e-06, 
                8.545e-06, 6.792e-06, 5.059e-06, 2.678e-06, 1.816e-06, 
                1.223e-06, 8.245e-07, 5.589e-07, -4.571e-06, -2.309e-05, 
                0.0, 8.545e-06, 9.182e-06, 7.219e-06, 5.388e-06, 
                2.853e-06, 1.944e-06, 1.324e-06, 9.083e-07, 6.335e-07, 
                -3.614e-06, -1.838e-05, 0.0, 6.792e-06, 7.219e-06, 
                6.016e-06, 4.437e-06, 2.385e-06, 1.636e-06, 1.118e-06, 
                7.754e-07, 5.556e-07, -2.636e-06, -1.373e-05, 0.0, 
                5.059e-06, 5.388e-06, 4.437e-06, 3.602e-06, 1.917e-06, 
                1.322e-06, 9.079e-07, 6.529e-07, 4.752e-07, -1.286e-06, 
                -7.334e-06, 0.0, 2.678e-06, 2.853e-06, 2.385e-06, 
                1.917e-06, 1.375e-06, 9.1e-07, 6.455e-07, 4.693e-07, 
                3.657e-07, -8.41e-07, -5.088e-06, 0.0, 1.816e-06, 
                1.944e-06, 1.636e-06, 1.322e-06, 9.1e-07, 9.115e-07, 
                6.062e-07, 4.436e-07, 3.422e-07, -5.296e-07, -3.745e-06, 
                0.0, 1.223e-06, 1.324e-06, 1.118e-06, 9.079e-07, 
                6.455e-07, 6.062e-07, 7.217e-07, 4.862e-07, 3.768e-07, 
                0.0, -2.428e-06, 0.0, 8.245e-07, 9.083e-07, 
                7.754e-07, 6.529e-07, 4.693e-07, 4.436e-07, 4.862e-07, 
                6.509e-07, 4.418e-07, 0.0, 0.0, 0.0, 
                5.589e-07, 6.335e-07, 5.556e-07, 4.752e-07, 3.657e-07, 
                3.422e-07, 3.768e-07, 4.418e-07, 6.142e-07),
            EBPulseShapeTemplate = cms.vdouble(0.0113979, 0.758151, 1.0, 0.887744, 0.673548, 
                0.474332, 0.319561, 0.215144, 0.147464, 0.101087, 
                0.0693181, 0.0475044),
            EBdigiCollection = cms.string(''),
            EECorrNoiseMatrixG01 = cms.vdouble(1.0, 0.72698, 0.62048, 0.55691, 0.51848, 
                0.49147, 0.47813, 0.47007, 0.46621, 0.46265),
            EECorrNoiseMatrixG06 = cms.vdouble(1.0, 0.71217, 0.47464, 0.34056, 0.26282, 
                0.20287, 0.17734, 0.16256, 0.15618, 0.14443),
            EECorrNoiseMatrixG12 = cms.vdouble(1.0, 0.71373, 0.44825, 0.30152, 0.21609, 
                0.14786, 0.11772, 0.10165, 0.09465, 0.08098),
            EEPulseShapeCovariance = cms.vdouble(3.941e-05, 3.333e-05, 0.0, -1.449e-05, -1.661e-05, 
                -1.424e-05, -1.183e-05, -6.842e-06, -4.915e-06, -3.411e-06, 
                0.0, 0.0, 3.333e-05, 2.862e-05, 0.0, 
                -1.244e-05, -1.431e-05, -1.233e-05, -1.032e-05, -5.883e-06, 
                -4.154e-06, -2.902e-06, -2.128e-06, 0.0, 0.0, 
                0.0, 0.0, 0.0, 0.0, 0.0, 
                0.0, 0.0, 0.0, 0.0, 0.0, 
                0.0, -1.449e-05, -1.244e-05, 0.0, 5.84e-06, 
                6.649e-06, 5.72e-06, 4.812e-06, 2.708e-06, 1.869e-06, 
                1.33e-06, 9.186e-07, 6.446e-07, -1.661e-05, -1.431e-05, 
                0.0, 6.649e-06, 7.966e-06, 6.898e-06, 5.794e-06, 
                3.157e-06, 2.184e-06, 1.567e-06, 1.084e-06, 7.575e-07, 
                -1.424e-05, -1.233e-05, 0.0, 5.72e-06, 6.898e-06, 
                6.341e-06, 5.347e-06, 2.859e-06, 1.991e-06, 1.431e-06, 
                9.839e-07, 6.886e-07, -1.183e-05, -1.032e-05, 0.0, 
                4.812e-06, 5.794e-06, 5.347e-06, 4.854e-06, 2.628e-06, 
                1.809e-06, 1.289e-06, 9.02e-07, 6.146e-07, -6.842e-06, 
                -5.883e-06, 0.0, 2.708e-06, 3.157e-06, 2.859e-06, 
                2.628e-06, 1.863e-06, 1.296e-06, 8.882e-07, 6.108e-07, 
                4.283e-07, -4.915e-06, -4.154e-06, 0.0, 1.869e-06, 
                2.184e-06, 1.991e-06, 1.809e-06, 1.296e-06, 1.217e-06, 
                8.669e-07, 5.751e-07, 3.882e-07, -3.411e-06, -2.902e-06, 
                0.0, 1.33e-06, 1.567e-06, 1.431e-06, 1.289e-06, 
                8.882e-07, 8.669e-07, 9.522e-07, 6.717e-07, 4.293e-07, 
                0.0, -2.128e-06, 0.0, 9.186e-07, 1.084e-06, 
                9.839e-07, 9.02e-07, 6.108e-07, 5.751e-07, 6.717e-07, 
                7.911e-07, 5.493e-07, 0.0, 0.0, 0.0, 
                6.446e-07, 7.575e-07, 6.886e-07, 6.146e-07, 4.283e-07, 
                3.882e-07, 4.293e-07, 5.493e-07, 7.027e-07),
            EEPulseShapeTemplate = cms.vdouble(0.116442, 0.756246, 1.0, 0.897182, 0.686831, 
                0.491506, 0.344111, 0.245731, 0.174115, 0.123361, 
                0.0874288, 0.061957),
            EEdigiCollection = cms.string(''),
            ESdigiCollection = cms.string(''),
            EcalPreMixStage1 = cms.bool(False),
            EcalPreMixStage2 = cms.bool(False),
            UseLCcorrection = cms.untracked.bool(True)
        ),
        activeBXs = cms.vint32(-5, -4, -3, -2, -1, 
            0, 1, 2, 3, 4),
        ampErrorCalculation = cms.bool(True),
        amplitudeThresholdEB = cms.double(10),
        amplitudeThresholdEE = cms.double(10),
        chi2ThreshEB_ = cms.double(65.0),
        chi2ThreshEE_ = cms.double(50.0),
        doPrefitEB = cms.bool(False),
        doPrefitEE = cms.bool(False),
        ebPulseShape = cms.vdouble(5.2e-05, -5.26e-05, 6.66e-05, 0.1168, 0.7575, 
            1.0, 0.8876, 0.6732, 0.4741, 0.3194),
        ebSpikeThreshold = cms.double(1.042),
        eePulseShape = cms.vdouble(5.2e-05, -5.26e-05, 6.66e-05, 0.1168, 0.7575, 
            1.0, 0.8876, 0.6732, 0.4741, 0.3194),
        kPoorRecoFlagEB = cms.bool(True),
        kPoorRecoFlagEE = cms.bool(False),
        outOfTimeThresholdGain12mEB = cms.double(5),
        outOfTimeThresholdGain12mEE = cms.double(1000),
        outOfTimeThresholdGain12pEB = cms.double(5),
        outOfTimeThresholdGain12pEE = cms.double(1000),
        outOfTimeThresholdGain61mEB = cms.double(5),
        outOfTimeThresholdGain61mEE = cms.double(1000),
        outOfTimeThresholdGain61pEB = cms.double(5),
        outOfTimeThresholdGain61pEE = cms.double(1000),
        prefitMaxChiSqEB = cms.double(25.0),
        prefitMaxChiSqEE = cms.double(10.0),
        timealgo = cms.string('RatioMethod'),
        useLumiInfoRunHeader = cms.bool(True)
    )
)


process.ecalPreshowerDigis = cms.EDProducer("ESRawToDigi",
    ESdigiCollection = cms.string(''),
    InstanceES = cms.string(''),
    LookupTable = cms.FileInPath('EventFilter/ESDigiToRaw/data/ES_lookup_table.dat'),
    debugMode = cms.untracked.bool(False),
    sourceTag = cms.InputTag("rawDataCollector")
)


process.ecalPreshowerRecHit = cms.EDProducer("ESRecHitProducer",
    ESRecoAlgo = cms.int32(0),
    ESdigiCollection = cms.InputTag("ecalPreshowerDigis"),
    ESrechitCollection = cms.string('EcalRecHitsES'),
    algo = cms.string('ESRecHitWorker')
)


process.ecalRecHit = cms.EDProducer("EcalRecHitProducer",
    ChannelStatusToBeExcluded = cms.vstring('kDAC', 
        'kNoisy', 
        'kNNoisy', 
        'kFixedG6', 
        'kFixedG1', 
        'kFixedG0', 
        'kNonRespondingIsolated', 
        'kDeadVFE', 
        'kDeadFE', 
        'kNoDataNoTP'),
    EBLaserMAX = cms.double(3.0),
    EBLaserMIN = cms.double(0.5),
    EBrechitCollection = cms.string('EcalRecHitsEB'),
    EBuncalibRecHitCollection = cms.InputTag("ecalMultiFitUncalibRecHit","EcalUncalibRecHitsEB"),
    EELaserMAX = cms.double(8.0),
    EELaserMIN = cms.double(0.5),
    EErechitCollection = cms.string('EcalRecHitsEE'),
    EEuncalibRecHitCollection = cms.InputTag("ecalMultiFitUncalibRecHit","EcalUncalibRecHitsEE"),
    algo = cms.string('EcalRecHitWorkerSimple'),
    algoRecover = cms.string('EcalRecHitWorkerRecover'),
    cleaningConfig = cms.PSet(
        cThreshold_barrel = cms.double(4),
        cThreshold_double = cms.double(10),
        cThreshold_endcap = cms.double(15),
        e4e1Threshold_barrel = cms.double(0.08),
        e4e1Threshold_endcap = cms.double(0.3),
        e4e1_a_barrel = cms.double(0.02),
        e4e1_a_endcap = cms.double(0.02),
        e4e1_b_barrel = cms.double(0.02),
        e4e1_b_endcap = cms.double(-0.0125),
        e6e2thresh = cms.double(0.04),
        ignoreOutOfTimeThresh = cms.double(1000000000.0),
        tightenCrack_e1_double = cms.double(2),
        tightenCrack_e1_single = cms.double(1),
        tightenCrack_e4e1_single = cms.double(2.5),
        tightenCrack_e6e2_double = cms.double(3)
    ),
    dbStatusToBeExcludedEB = cms.vint32(14, 78, 142),
    dbStatusToBeExcludedEE = cms.vint32(14, 78, 142),
    ebDetIdToBeRecovered = cms.InputTag("ecalDetIdToBeRecovered","ebDetId"),
    ebFEToBeRecovered = cms.InputTag("ecalDetIdToBeRecovered","ebFE"),
    eeDetIdToBeRecovered = cms.InputTag("ecalDetIdToBeRecovered","eeDetId"),
    eeFEToBeRecovered = cms.InputTag("ecalDetIdToBeRecovered","eeFE"),
    flagsMapDBReco = cms.PSet(
        kDead = cms.vstring('kNoDataNoTP'),
        kGood = cms.vstring('kOk', 
            'kDAC', 
            'kNoLaser', 
            'kNoisy'),
        kNeighboursRecovered = cms.vstring('kFixedG0', 
            'kNonRespondingIsolated', 
            'kDeadVFE'),
        kNoisy = cms.vstring('kNNoisy', 
            'kFixedG6', 
            'kFixedG1'),
        kTowerRecovered = cms.vstring('kDeadFE')
    ),
    killDeadChannels = cms.bool(True),
    laserCorrection = cms.bool(True),
    logWarningEtThreshold_EB_FE = cms.double(50),
    logWarningEtThreshold_EE_FE = cms.double(50),
    recoverEBFE = cms.bool(True),
    recoverEBIsolatedChannels = cms.bool(False),
    recoverEBVFE = cms.bool(False),
    recoverEEFE = cms.bool(True),
    recoverEEIsolatedChannels = cms.bool(False),
    recoverEEVFE = cms.bool(False),
    singleChannelRecoveryMethod = cms.string('NeuralNetworks'),
    singleChannelRecoveryThreshold = cms.double(8),
    triggerPrimitiveDigiCollection = cms.InputTag("ecalDigis","EcalTriggerPrimitives")
)


process.ecalTPSkim = cms.EDProducer("EcalTPSkimmer",
    chStatusToSelectTP = cms.vuint32(13),
    doBarrel = cms.bool(True),
    doEndcap = cms.bool(True),
    skipModule = cms.bool(False),
    tpInputCollection = cms.InputTag("ecalDigis","EcalTriggerPrimitives"),
    tpOutputCollection = cms.string('')
)


process.elPFIsoDepositChargedAllGsf = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedParticles")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositChargedGsf = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedHadrons")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositGammaGsf = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFCandWithSuperClusterExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        MissHitSCMatch_Veto = cms.bool(True),
        SCMatch_Veto = cms.bool(False),
        inputCandView = cms.InputTag("pfAllPhotons")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositNeutralGsf = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllNeutralHadrons")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositPUGsf = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfPileUpAllChargedParticles")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons"),
    trackType = cms.string('candidate')
)


process.elPFIsoValueCharged03PFIdGsf = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedGsf"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll03PFIdGsf = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAllGsf"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma03PFIdGsf = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGammaGsf"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral03PFIdGsf = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutralGsf"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU03PFIdGsf = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPUGsf"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.eleNewEnergiesProducer = cms.EDProducer("EleNewEnergiesProducer",
    electronCollection = cms.InputTag("slimmedElectrons"),
    photonCollection = cms.InputTag("slimmedPhotons","","@skipCurrentProcess"),
    recHitCollectionEB = cms.InputTag("alCaIsolatedElectrons","alcaBarrelHits"),
    recHitCollectionEE = cms.InputTag("alCaIsolatedElectrons","alcaEndcapHits"),
    scEnergyCorrectorSemiParm = cms.PSet(
        ecalRecHitsEB = cms.InputTag("reducedEgamma","reducedEBRecHits"),
        ecalRecHitsEE = cms.InputTag("reducedEgamma","reducedEERecHits"),
        isHLT = cms.bool(False),
        regressionKeyEB = cms.string('pfscecal_EBCorrection_offline_v2'),
        regressionKeyEE = cms.string('pfscecal_EECorrection_offline_v2'),
        uncertaintyKeyEB = cms.string('pfscecal_EBUncertainty_offline_v2'),
        uncertaintyKeyEE = cms.string('pfscecal_EEUncertainty_offline_v2'),
        vertexCollection = cms.InputTag("offlineSlimmedPrimaryVertices")
    )
)


process.eleSC = cms.EDProducer("ConcreteEcalCandidateProducer",
    particleType = cms.string('gamma'),
    src = cms.InputTag("SCselector")
)


process.eleSelectionProducers = cms.EDProducer("EleSelectionProducers",
    BeamSpotCollection = cms.InputTag("offlineBeamSpot"),
    chIsoVals = cms.InputTag("elPFIsoValueCharged03PFIdPFIso"),
    conversionCollection = cms.InputTag("reducedEgamma","reducedConversions"),
    electronCollection = cms.InputTag("slimmedElectrons"),
    emIsoVals = cms.InputTag("elPFIsoValueGamma03PFIdPFIso"),
    nhIsoVals = cms.InputTag("elPFIsoValueNeutral03PFIdPFIso"),
    rhoFastJet = cms.InputTag("fixedGridRhoFastjetAll"),
    vertexCollection = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.electronMVAValueMapProducer = cms.EDProducer("ElectronMVAValueMapProducer",
    mvaConfigurations = cms.VPSet(cms.PSet(
        mvaName = cms.string('ElectronMVAEstimatorRun2Phys14NonTrig'),
        mvaTag = cms.string('25nsV1'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_5_oldscenario2phys14_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_5_oldscenario2phys14_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_5_oldscenario2phys14_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_10_oldscenario2phys14_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_10_oldscenario2phys14_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_10_oldscenario2phys14_BDT.weights.xml')
    ), 
        cms.PSet(
            beamSpot = cms.InputTag("offlineBeamSpot"),
            conversionsAOD = cms.InputTag("allConversions"),
            conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
            mvaName = cms.string('ElectronMVAEstimatorRun2Spring15NonTrig'),
            mvaTag = cms.string('25nsV1'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml')
        ), 
        cms.PSet(
            beamSpot = cms.InputTag("offlineBeamSpot"),
            conversionsAOD = cms.InputTag("allConversions"),
            conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
            mvaName = cms.string('ElectronMVAEstimatorRun2Spring15Trig'),
            mvaTag = cms.string('50nsV1'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml')
        ), 
        cms.PSet(
            beamSpot = cms.InputTag("offlineBeamSpot"),
            conversionsAOD = cms.InputTag("allConversions"),
            conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
            mvaName = cms.string('ElectronMVAEstimatorRun2Spring15Trig'),
            mvaTag = cms.string('25nsV1'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml')
        )),
    src = cms.InputTag("gedGsfElectrons"),
    srcMiniAOD = cms.InputTag("slimmedElectrons","","@skipCurrentProcess")
)


process.electronMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(0.5),
    maxDeltaR = cms.double(0.5),
    mcPdgId = cms.vint32(11),
    mcStatus = cms.vint32(1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("slimmedElectrons")
)


process.electronRecalibSCAssociator = cms.EDProducer("ElectronRecalibSuperClusterAssociator",
    electronSrc = cms.InputTag("gedGsfElectrons"),
    outputLabel = cms.string('recalibSC'),
    superClusterCollectionEB = cms.InputTag("particleFlowSuperClusterECAL","particleFlowSuperClusterECALBarrel"),
    superClusterCollectionEE = cms.InputTag("particleFlowSuperClusterECAL","particleFlowSuperClusterECALEndcapWithPreshower")
)


process.gctDigis = cms.EDProducer("GctRawToDigi",
    checkHeaders = cms.untracked.bool(False),
    gctFedId = cms.untracked.int32(745),
    hltMode = cms.bool(False),
    inputLabel = cms.InputTag("rawDataCollector"),
    numberOfGctSamplesToUnpack = cms.uint32(1),
    numberOfRctSamplesToUnpack = cms.uint32(1),
    unpackSharedRegions = cms.bool(False),
    unpackerVersion = cms.uint32(0),
    verbose = cms.untracked.bool(False)
)


process.gtDigis = cms.EDProducer("L1GlobalTriggerRawToDigi",
    ActiveBoardsMask = cms.uint32(65535),
    DaqGtFedId = cms.untracked.int32(813),
    DaqGtInputTag = cms.InputTag("rawDataCollector"),
    UnpackBxInEvent = cms.int32(-1),
    Verbosity = cms.untracked.int32(0)
)


process.gtEvmDigis = cms.EDProducer("L1GlobalTriggerEvmRawToDigi",
    ActiveBoardsMask = cms.uint32(65535),
    BstLengthBytes = cms.int32(-1),
    EvmGtFedId = cms.untracked.int32(812),
    EvmGtInputTag = cms.InputTag("rawDataCollector"),
    UnpackBxInEvent = cms.int32(-1)
)


process.hbheprereco = cms.EDProducer("HcalHitReconstructor",
    Subdetector = cms.string('HBHE'),
    applyPedConstraint = cms.bool(True),
    applyPulseJitter = cms.bool(False),
    applyTimeConstraint = cms.bool(True),
    applyTimeSlew = cms.bool(True),
    applyUnconstrainedFit = cms.bool(False),
    chargeMax = cms.double(6.0),
    correctForPhaseContainment = cms.bool(True),
    correctForTimeslew = cms.bool(True),
    correctTiming = cms.bool(True),
    correctionPhaseNS = cms.double(6.0),
    dataOOTCorrectionCategory = cms.string('Data'),
    dataOOTCorrectionName = cms.string('HBHE'),
    digiLabel = cms.InputTag("hcalDigis"),
    dropZSmarkedPassed = cms.bool(True),
    firstAuxTS = cms.int32(4),
    firstSample = cms.int32(4),
    fitTimes = cms.int32(1),
    flagParameters = cms.PSet(
        hitEnergyMinimum = cms.double(1.0),
        hitMultiplicityThreshold = cms.int32(17),
        nominalPedestal = cms.double(3.0),
        pulseShapeParameterSets = cms.VPSet(cms.PSet(
            pulseShapeParameters = cms.vdouble(0.0, 100.0, -50.0, 0.0, -15.0, 
                0.15)
        ), 
            cms.PSet(
                pulseShapeParameters = cms.vdouble(100.0, 2000.0, -50.0, 0.0, -5.0, 
                    0.05)
            ), 
            cms.PSet(
                pulseShapeParameters = cms.vdouble(2000.0, 1000000.0, -50.0, 0.0, 95.0, 
                    0.0)
            ), 
            cms.PSet(
                pulseShapeParameters = cms.vdouble(-1000000.0, 1000000.0, 45.0, 0.1, 1000000.0, 
                    0.0)
            ))
    ),
    hscpParameters = cms.PSet(
        TimingEnergyThreshold = cms.double(30.0),
        fracLeaderMax = cms.double(0.7),
        fracLeaderMin = cms.double(0.4),
        outerMax = cms.double(0.1),
        outerMin = cms.double(0.0),
        r1Max = cms.double(1.0),
        r1Min = cms.double(0.15),
        r2Max = cms.double(0.5),
        r2Min = cms.double(0.1),
        slopeMax = cms.double(-0.6),
        slopeMin = cms.double(-1.5)
    ),
    mcOOTCorrectionCategory = cms.string('MC'),
    mcOOTCorrectionName = cms.string('HBHE'),
    meanPed = cms.double(0.0),
    meanTime = cms.double(0.0),
    noise = cms.double(1),
    pedSigma = cms.double(0.5),
    pedestalSubtractionType = cms.int32(1),
    pedestalUpperLimit = cms.double(2.7),
    puCorrMethod = cms.int32(2),
    pulseJitter = cms.double(1.0),
    pulseShapeParameters = cms.PSet(
        LeftSlopeCut = cms.vdouble(5, 2.55, 2.55),
        LeftSlopeThreshold = cms.vdouble(250, 500, 100000),
        LinearCut = cms.vdouble(-3, -0.054, -0.054),
        LinearThreshold = cms.vdouble(20, 100, 100000),
        MinimumChargeThreshold = cms.double(20),
        MinimumTS4TS5Threshold = cms.double(100),
        R45MinusOneRange = cms.double(0.2),
        R45PlusOneRange = cms.double(0.2),
        RMS8MaxCut = cms.vdouble(-13.5, -11.5, -11.5),
        RMS8MaxThreshold = cms.vdouble(20, 100, 100000),
        RightSlopeCut = cms.vdouble(5, 4.15, 4.15),
        RightSlopeSmallCut = cms.vdouble(1.08, 1.16, 1.16),
        RightSlopeSmallThreshold = cms.vdouble(150, 200, 100000),
        RightSlopeThreshold = cms.vdouble(250, 400, 100000),
        TS3TS4ChargeThreshold = cms.double(70),
        TS3TS4UpperChargeThreshold = cms.double(20),
        TS4TS5ChargeThreshold = cms.double(70),
        TS4TS5LowerCut = cms.vdouble(-1, -0.7, -0.5, -0.4, -0.3, 
            0.1),
        TS4TS5LowerThreshold = cms.vdouble(100, 120, 160, 200, 300, 
            500),
        TS4TS5UpperCut = cms.vdouble(1, 0.8, 0.75, 0.72),
        TS4TS5UpperThreshold = cms.vdouble(70, 90, 100, 400),
        TS5TS6ChargeThreshold = cms.double(70),
        TS5TS6UpperChargeThreshold = cms.double(20),
        TriangleIgnoreSlow = cms.bool(False),
        TrianglePeakTS = cms.uint32(4),
        UseDualFit = cms.bool(True)
    ),
    recoParamsFromDB = cms.bool(True),
    respCorrM3 = cms.double(0.95),
    samplesToAdd = cms.int32(2),
    saturationParameters = cms.PSet(
        maxADCvalue = cms.int32(127)
    ),
    setHSCPFlags = cms.bool(True),
    setNegativeFlags = cms.bool(True),
    setNoiseFlags = cms.bool(True),
    setPulseShapeFlags = cms.bool(True),
    setSaturationFlags = cms.bool(True),
    setTimingShapedCutsFlags = cms.bool(True),
    setTimingTrustFlags = cms.bool(False),
    timeMax = cms.double(12.5),
    timeMin = cms.double(-12.5),
    timeSigma = cms.double(5.0),
    timeSlewPars = cms.vdouble(12.2999, -2.19142, 0, 12.2999, -2.19142, 
        0, 12.2999, -2.19142, 0),
    timeSlewParsType = cms.int32(1),
    timingshapedcutsParameters = cms.PSet(
        ignorehighest = cms.bool(False),
        ignorelowest = cms.bool(True),
        tfilterEnvelope = cms.vdouble(50.0, -2.0, 4.25, 52.0, -2.0, 
            4.09, 54.0, -2.0, 3.95, 56.0, 
            -2.0, 3.82, 58.0, -2.0, 3.71, 
            60.0, -2.0, 3.6, 63.0, -2.0, 
            3.46, 66.0, -2.0, 3.33, 69.0, 
            -2.0, 3.22, 73.0, -2.0, 3.1, 
            77.0, -2.0, 2.99, 82.0, -2.0, 
            2.87, 88.0, -2.0, 2.75, 95.0, 
            -2.0, 2.64, 103.0, -2.0, 2.54, 
            113.0, -2.0, 2.44, 127.0, -2.0, 
            2.33, 146.0, -2.0, 2.23, 176.0, 
            -2.0, 2.13, 250.0, -2.0, 2.0),
        win_gain = cms.double(3.0),
        win_offset = cms.double(0.0)
    ),
    ts345chi2 = cms.double(100.0),
    ts3chi2 = cms.double(5.0),
    ts4Max = cms.double(100.0),
    ts4Min = cms.double(0.0),
    ts4chi2 = cms.double(15.0),
    tsFromDB = cms.bool(True),
    useLeakCorrection = cms.bool(False)
)


process.hbhereco = cms.EDProducer("HBHEIsolatedNoiseReflagger",
    EBThreshold = cms.double(0.07),
    EEThreshold = cms.double(0.3),
    EcalAcceptSeverityLevel = cms.uint32(3),
    HBThreshold = cms.double(0.7),
    HEDThreshold = cms.double(0.8),
    HESThreshold = cms.double(0.8),
    HcalAcceptSeverityLevel = cms.uint32(9),
    LooseDiHitEne = cms.double(50.0),
    LooseEcalIsol = cms.double(0.08),
    LooseHPDEne1 = cms.double(20.0),
    LooseHPDEne2 = cms.double(80.0),
    LooseHPDHits1 = cms.int32(6),
    LooseHPDHits2 = cms.int32(3),
    LooseHcalIsol = cms.double(0.08),
    LooseMonoHitEne = cms.double(35.0),
    LooseRBXEne1 = cms.double(30.0),
    LooseRBXEne2 = cms.double(160.0),
    LooseRBXHits1 = cms.int32(14),
    LooseRBXHits2 = cms.int32(6),
    LooseTrackIsol = cms.double(0.1),
    MinValidTrackNHits = cms.int32(5),
    MinValidTrackPt = cms.double(0.3),
    MinValidTrackPtBarrel = cms.double(0.9),
    RBXEneThreshold = cms.double(500.0),
    TightDiHitEne = cms.double(15.0),
    TightEcalIsol = cms.double(0.04),
    TightHPDEne1 = cms.double(10.0),
    TightHPDEne2 = cms.double(30.0),
    TightHPDHits1 = cms.int32(6),
    TightHPDHits2 = cms.int32(3),
    TightHcalIsol = cms.double(0.04),
    TightMonoHitEne = cms.double(15.0),
    TightRBXEne1 = cms.double(25.0),
    TightRBXEne2 = cms.double(60.0),
    TightRBXHits1 = cms.int32(12),
    TightRBXHits2 = cms.int32(7),
    TightTrackIsol = cms.double(0.05),
    UseEcalRecoveredHits = cms.bool(False),
    UseHcalRecoveredHits = cms.bool(True),
    debug = cms.untracked.bool(False),
    ebInput = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    eeInput = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    hbheInput = cms.InputTag("hbheprereco"),
    trackExtrapolationInput = cms.InputTag("trackExtrapolator")
)


process.hbherecoMB = cms.EDProducer("HcalSimpleReconstructor",
    Subdetector = cms.string('HBHE'),
    correctForPhaseContainment = cms.bool(True),
    correctForTimeslew = cms.bool(True),
    correctionPhaseNS = cms.double(13.0),
    digiLabel = cms.InputTag("hcalDigis"),
    dropZSmarkedPassed = cms.bool(False),
    firstSample = cms.int32(4),
    pedestalSubtractionType = cms.int32(1),
    pedestalUpperLimit = cms.double(2.7),
    respCorrM3 = cms.double(0.95),
    samplesToAdd = cms.int32(4),
    timeSlewPars = cms.vdouble(12.2999, -2.19142, 0, 12.2999, -2.19142, 
        0, 12.2999, -2.19142, 0),
    timeSlewParsType = cms.int32(1),
    tsFromDB = cms.bool(True)
)


process.hcalDigis = cms.EDProducer("HcalRawToDigi",
    ComplainEmptyData = cms.untracked.bool(False),
    ElectronicsMap = cms.string(''),
    ExpectedOrbitMessageTime = cms.untracked.int32(-1),
    FEDs = cms.untracked.vint32(),
    FilterDataQuality = cms.bool(True),
    HcalFirstFED = cms.untracked.int32(700),
    InputLabel = cms.InputTag("rawDataCollector"),
    UnpackCalib = cms.untracked.bool(True),
    UnpackTTP = cms.untracked.bool(True),
    UnpackZDC = cms.untracked.bool(True),
    UnpackerMode = cms.untracked.int32(0),
    firstSample = cms.int32(0),
    lastSample = cms.int32(9),
    silent = cms.untracked.bool(True)
)


process.hfreco = cms.EDProducer("HcalHitReconstructor",
    HFInWindowStat = cms.PSet(
        hflongEthresh = cms.double(40.0),
        hflongMaxWindowTime = cms.vdouble(10),
        hflongMinWindowTime = cms.vdouble(-10),
        hfshortEthresh = cms.double(40.0),
        hfshortMaxWindowTime = cms.vdouble(10),
        hfshortMinWindowTime = cms.vdouble(-12)
    ),
    PETstat = cms.PSet(
        HcalAcceptSeverityLevel = cms.int32(9),
        longETParams = cms.vdouble(0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 
            0, 0, 0),
        longEnergyParams = cms.vdouble(43.5, 45.7, 48.32, 51.36, 54.82, 
            58.7, 63.0, 67.72, 72.86, 78.42, 
            84.4, 90.8, 97.62),
        long_R = cms.vdouble(0.98),
        long_R_29 = cms.vdouble(0.8),
        shortETParams = cms.vdouble(0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 
            0, 0, 0),
        shortEnergyParams = cms.vdouble(35.1773, 35.37, 35.7933, 36.4472, 37.3317, 
            38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 
            47.4813, 49.98, 52.7093),
        short_R = cms.vdouble(0.8),
        short_R_29 = cms.vdouble(0.8)
    ),
    S8S1stat = cms.PSet(
        HcalAcceptSeverityLevel = cms.int32(9),
        isS8S1 = cms.bool(True),
        longETParams = cms.vdouble(0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 
            0, 0, 0),
        longEnergyParams = cms.vdouble(40, 100, 100, 100, 100, 
            100, 100, 100, 100, 100, 
            100, 100, 100),
        long_optimumSlope = cms.vdouble(0.3, 0.1, 0.1, 0.1, 0.1, 
            0.1, 0.1, 0.1, 0.1, 0.1, 
            0.1, 0.1, 0.1),
        shortETParams = cms.vdouble(0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 
            0, 0, 0),
        shortEnergyParams = cms.vdouble(40, 100, 100, 100, 100, 
            100, 100, 100, 100, 100, 
            100, 100, 100),
        short_optimumSlope = cms.vdouble(0.3, 0.1, 0.1, 0.1, 0.1, 
            0.1, 0.1, 0.1, 0.1, 0.1, 
            0.1, 0.1, 0.1)
    ),
    S9S1stat = cms.PSet(
        HcalAcceptSeverityLevel = cms.int32(9),
        isS8S1 = cms.bool(False),
        longETParams = cms.vdouble(0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 
            0, 0, 0),
        longEnergyParams = cms.vdouble(43.5, 45.7, 48.32, 51.36, 54.82, 
            58.7, 63.0, 67.72, 72.86, 78.42, 
            84.4, 90.8, 97.62),
        long_optimumSlope = cms.vdouble(-99999, 0.0164905, 0.0238698, 0.0321383, 0.041296, 
            0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 
            0.135313, 0.136289, 0.0589927),
        shortETParams = cms.vdouble(0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 
            0, 0, 0),
        shortEnergyParams = cms.vdouble(35.1773, 35.37, 35.7933, 36.4472, 37.3317, 
            38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 
            47.4813, 49.98, 52.7093),
        short_optimumSlope = cms.vdouble(-99999, 0.0164905, 0.0238698, 0.0321383, 0.041296, 
            0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 
            0.135313, 0.136289, 0.0589927)
    ),
    Subdetector = cms.string('HF'),
    correctForPhaseContainment = cms.bool(False),
    correctForTimeslew = cms.bool(False),
    correctTiming = cms.bool(True),
    correctionPhaseNS = cms.double(13.0),
    dataOOTCorrectionCategory = cms.string('Data'),
    dataOOTCorrectionName = cms.string(''),
    digiLabel = cms.InputTag("hcalDigis"),
    digiTimeFromDB = cms.bool(True),
    digistat = cms.PSet(
        HFdigiflagCoef = cms.vdouble(0.93, -0.38275, -0.012667),
        HFdigiflagExpectedPeak = cms.int32(2),
        HFdigiflagFirstSample = cms.int32(1),
        HFdigiflagMinEthreshold = cms.double(40),
        HFdigiflagSamplesToAdd = cms.int32(3)
    ),
    dropZSmarkedPassed = cms.bool(True),
    firstAuxTS = cms.int32(1),
    firstSample = cms.int32(2),
    hfTimingTrustParameters = cms.PSet(
        hfTimingTrustLevel1 = cms.int32(1),
        hfTimingTrustLevel2 = cms.int32(4)
    ),
    mcOOTCorrectionCategory = cms.string('MC'),
    mcOOTCorrectionName = cms.string(''),
    puCorrMethod = cms.int32(0),
    recoParamsFromDB = cms.bool(True),
    samplesToAdd = cms.int32(1),
    saturationParameters = cms.PSet(
        maxADCvalue = cms.int32(127)
    ),
    setHSCPFlags = cms.bool(False),
    setNegativeFlags = cms.bool(False),
    setNoiseFlags = cms.bool(True),
    setPulseShapeFlags = cms.bool(False),
    setSaturationFlags = cms.bool(True),
    setTimingTrustFlags = cms.bool(True),
    tsFromDB = cms.bool(True),
    useLeakCorrection = cms.bool(False)
)


process.hfrecoMB = cms.EDProducer("HcalSimpleReconstructor",
    Subdetector = cms.string('HF'),
    correctForPhaseContainment = cms.bool(False),
    correctForTimeslew = cms.bool(False),
    correctionPhaseNS = cms.double(0.0),
    digiLabel = cms.InputTag("hcalDigis"),
    dropZSmarkedPassed = cms.bool(False),
    firstSample = cms.int32(4),
    samplesToAdd = cms.int32(2),
    tsFromDB = cms.bool(True)
)


process.horeco = cms.EDProducer("HcalHitReconstructor",
    Subdetector = cms.string('HO'),
    correctForPhaseContainment = cms.bool(True),
    correctForTimeslew = cms.bool(True),
    correctTiming = cms.bool(True),
    correctionPhaseNS = cms.double(13.0),
    dataOOTCorrectionCategory = cms.string('Data'),
    dataOOTCorrectionName = cms.string(''),
    digiLabel = cms.InputTag("hcalDigis"),
    dropZSmarkedPassed = cms.bool(True),
    firstAuxTS = cms.int32(4),
    firstSample = cms.int32(4),
    mcOOTCorrectionCategory = cms.string('MC'),
    mcOOTCorrectionName = cms.string(''),
    puCorrMethod = cms.int32(0),
    recoParamsFromDB = cms.bool(True),
    samplesToAdd = cms.int32(4),
    saturationParameters = cms.PSet(
        maxADCvalue = cms.int32(127)
    ),
    setHSCPFlags = cms.bool(True),
    setNegativeFlags = cms.bool(False),
    setNoiseFlags = cms.bool(True),
    setPulseShapeFlags = cms.bool(False),
    setSaturationFlags = cms.bool(True),
    setTimingTrustFlags = cms.bool(False),
    tsFromDB = cms.bool(True),
    useLeakCorrection = cms.bool(False)
)


process.horecoMB = cms.EDProducer("HcalSimpleReconstructor",
    Subdetector = cms.string('HO'),
    correctForPhaseContainment = cms.bool(True),
    correctForTimeslew = cms.bool(True),
    correctionPhaseNS = cms.double(13.0),
    digiLabel = cms.InputTag("hcalDigis"),
    dropZSmarkedPassed = cms.bool(False),
    firstSample = cms.int32(4),
    samplesToAdd = cms.int32(4),
    tsFromDB = cms.bool(True)
)


process.hybridSuperClusters = cms.EDProducer("UnifiedSCCollectionProducer",
    bcCollection = cms.string('hybridBarrelBasicClusters'),
    bcCollectionUncleanOnly = cms.string('uncleanOnlyHybridBarrelBasicClusters'),
    cleanBcCollection = cms.InputTag("cleanedHybridSuperClusters","hybridBarrelBasicClusters"),
    cleanScCollection = cms.InputTag("cleanedHybridSuperClusters"),
    scCollection = cms.string(''),
    scCollectionUncleanOnly = cms.string('uncleanOnlyHybridSuperClusters'),
    uncleanBcCollection = cms.InputTag("uncleanedHybridSuperClusters","hybridBarrelBasicClusters"),
    uncleanScCollection = cms.InputTag("uncleanedHybridSuperClusters")
)


process.interestingDetIdCollectionProducer = cms.EDProducer("InterestingDetIdCollectionProducer",
    basicClustersLabel = cms.InputTag(""),
    etaSize = cms.int32(5),
    interestingDetIdCollection = cms.string(''),
    keepNextToBoundary = cms.bool(True),
    keepNextToDead = cms.bool(True),
    phiSize = cms.int32(5),
    recHitsLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    severityLevel = cms.int32(1)
)


process.interestingEcalDetIdEB = cms.EDProducer("InterestingDetIdCollectionProducer",
    basicClustersLabel = cms.InputTag("hybridSuperClusters","hybridBarrelBasicClusters"),
    etaSize = cms.int32(5),
    interestingDetIdCollection = cms.string(''),
    keepNextToBoundary = cms.bool(True),
    keepNextToDead = cms.bool(True),
    phiSize = cms.int32(5),
    recHitsLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    severityLevel = cms.int32(1)
)


process.interestingEcalDetIdEBU = cms.EDProducer("InterestingDetIdCollectionProducer",
    basicClustersLabel = cms.InputTag("hybridSuperClusters","uncleanOnlyHybridBarrelBasicClusters"),
    etaSize = cms.int32(5),
    interestingDetIdCollection = cms.string(''),
    keepNextToBoundary = cms.bool(True),
    keepNextToDead = cms.bool(True),
    phiSize = cms.int32(5),
    recHitsLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    severityLevel = cms.int32(1)
)


process.interestingEcalDetIdEE = cms.EDProducer("InterestingDetIdCollectionProducer",
    basicClustersLabel = cms.InputTag("multi5x5SuperClusters","multi5x5EndcapBasicClusters"),
    etaSize = cms.int32(5),
    interestingDetIdCollection = cms.string(''),
    keepNextToBoundary = cms.bool(True),
    keepNextToDead = cms.bool(True),
    phiSize = cms.int32(5),
    recHitsLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    severityLevel = cms.int32(1)
)


process.interestingEcalDetIdPFEB = cms.EDProducer("InterestingDetIdCollectionProducer",
    basicClustersLabel = cms.InputTag("particleFlowSuperClusterECAL","particleFlowBasicClusterECALBarrel"),
    etaSize = cms.int32(5),
    interestingDetIdCollection = cms.string(''),
    keepNextToBoundary = cms.bool(True),
    keepNextToDead = cms.bool(True),
    phiSize = cms.int32(5),
    recHitsLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    severityLevel = cms.int32(1)
)


process.interestingEcalDetIdPFEE = cms.EDProducer("InterestingDetIdCollectionProducer",
    basicClustersLabel = cms.InputTag("particleFlowSuperClusterECAL","particleFlowBasicClusterECALEndcap"),
    etaSize = cms.int32(5),
    interestingDetIdCollection = cms.string(''),
    keepNextToBoundary = cms.bool(True),
    keepNextToDead = cms.bool(True),
    phiSize = cms.int32(5),
    recHitsLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    severityLevel = cms.int32(1)
)


process.interestingEcalDetIdPFES = cms.EDProducer("InterestingDetIdCollectionProducer",
    basicClustersLabel = cms.InputTag("particleFlowSuperClusterECAL","particleFlowBasicClusterECALPreshower"),
    etaSize = cms.int32(5),
    interestingDetIdCollection = cms.string(''),
    keepNextToBoundary = cms.bool(False),
    keepNextToDead = cms.bool(False),
    phiSize = cms.int32(5),
    recHitsLabel = cms.InputTag("ecalPreshowerRecHit","EcalRecHitsES"),
    severityLevel = cms.int32(-1)
)


process.interestingEcalDetIdRefinedEB = cms.EDProducer("InterestingDetIdCollectionProducer",
    basicClustersLabel = cms.InputTag("particleFlowEGamma","EBEEClusters"),
    etaSize = cms.int32(5),
    interestingDetIdCollection = cms.string(''),
    keepNextToBoundary = cms.bool(True),
    keepNextToDead = cms.bool(True),
    phiSize = cms.int32(5),
    recHitsLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    severityLevel = cms.int32(1)
)


process.interestingEcalDetIdRefinedEE = cms.EDProducer("InterestingDetIdCollectionProducer",
    basicClustersLabel = cms.InputTag("particleFlowEGamma","EBEEClusters"),
    etaSize = cms.int32(5),
    interestingDetIdCollection = cms.string(''),
    keepNextToBoundary = cms.bool(True),
    keepNextToDead = cms.bool(True),
    phiSize = cms.int32(5),
    recHitsLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    severityLevel = cms.int32(1)
)


process.interestingEcalDetIdRefinedES = cms.EDProducer("InterestingDetIdCollectionProducer",
    basicClustersLabel = cms.InputTag("particleFlowEGamma","ESClusters"),
    etaSize = cms.int32(5),
    interestingDetIdCollection = cms.string(''),
    keepNextToBoundary = cms.bool(False),
    keepNextToDead = cms.bool(False),
    phiSize = cms.int32(5),
    recHitsLabel = cms.InputTag("ecalPreshowerRecHit","EcalRecHitsES"),
    severityLevel = cms.int32(-1)
)


process.interestingTrackEcalDetIds = cms.EDProducer("InterestingTrackEcalDetIdProducer",
    MinTrackPt = cms.double(50.0),
    TrackAssociatorParameters = cms.PSet(
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        accountForTrajectoryChangeCalo = cms.bool(False),
        dREcal = cms.double(9999.0),
        dREcalPreselection = cms.double(0.05),
        dRHcal = cms.double(9999.0),
        dRHcalPreselection = cms.double(0.2),
        dRMuon = cms.double(9999.0),
        dRMuonPreselection = cms.double(0.2),
        dRPreshowerPreselection = cms.double(0.2),
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        propagateAllDirections = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        truthMatch = cms.bool(False),
        useCalo = cms.bool(False),
        useEcal = cms.bool(True),
        useHO = cms.bool(True),
        useHcal = cms.bool(True),
        useMuon = cms.bool(True),
        usePreshower = cms.bool(False)
    ),
    TrackCollection = cms.InputTag("generalTracks")
)


process.isoDeposits = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag(""),
    trackType = cms.string('candidate')
)


process.kt6PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('Kt'),
    jetPtMin = cms.double(5.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.6),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("particleFlow"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(0.9)
)


process.kt6PFJetsForRhoCorrection = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(2.5),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('Kt'),
    jetPtMin = cms.double(5.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.6),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("particleFlow"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(0.9)
)


process.modifiedElectrons = cms.EDProducer("ModifiedElectronProducer",
    modifierConfig = cms.PSet(
        modifications = cms.VPSet()
    ),
    src = cms.InputTag("slimmedElectrons","","@skipCurrentProcess")
)


process.modifiedJets = cms.EDProducer("ModifiedJetProducer",
    modifierConfig = cms.PSet(
        modifications = cms.VPSet()
    ),
    src = cms.InputTag("slimmedJets","","@skipCurrentProcess")
)


process.modifiedMuons = cms.EDProducer("ModifiedMuonProducer",
    modifierConfig = cms.PSet(
        modifications = cms.VPSet()
    ),
    src = cms.InputTag("slimmedMuons","","@skipCurrentProcess")
)


process.modifiedPhotons = cms.EDProducer("ModifiedPhotonProducer",
    modifierConfig = cms.PSet(
        modifications = cms.VPSet()
    ),
    src = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
)


process.modifiedTaus = cms.EDProducer("ModifiedTauProducer",
    modifierConfig = cms.PSet(
        modifications = cms.VPSet()
    ),
    src = cms.InputTag("slimmedTaus","","@skipCurrentProcess")
)


process.multi5x5BasicClustersCleaned = cms.EDProducer("Multi5x5ClusterProducer",
    IslandBarrelSeedThr = cms.double(0.5),
    IslandEndcapSeedThr = cms.double(0.18),
    RecHitFlagToBeExcluded = cms.vstring('kFaultyHardware', 
        'kNeighboursRecovered', 
        'kTowerRecovered', 
        'kDead', 
        'kWeird'),
    barrelClusterCollection = cms.string('multi5x5BarrelBasicClusters'),
    barrelHitTag = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    doBarrel = cms.bool(False),
    doEndcap = cms.bool(True),
    endcapClusterCollection = cms.string('multi5x5EndcapBasicClusters'),
    endcapHitTag = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    posCalcParameters = cms.PSet(
        LogWeighted = cms.bool(True),
        T0_barl = cms.double(7.4),
        T0_endc = cms.double(3.1),
        T0_endcPresh = cms.double(1.2),
        W0 = cms.double(4.2),
        X0 = cms.double(0.89)
    ),
    reassignSeedCrysToClusterItSeeds = cms.bool(True)
)


process.multi5x5BasicClustersUncleaned = cms.EDProducer("Multi5x5ClusterProducer",
    IslandBarrelSeedThr = cms.double(0.5),
    IslandEndcapSeedThr = cms.double(0.18),
    RecHitFlagToBeExcluded = cms.vstring(),
    barrelClusterCollection = cms.string('multi5x5BarrelBasicClusters'),
    barrelHitTag = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    doBarrel = cms.bool(False),
    doEndcap = cms.bool(True),
    endcapClusterCollection = cms.string('multi5x5EndcapBasicClusters'),
    endcapHitTag = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    posCalcParameters = cms.PSet(
        LogWeighted = cms.bool(True),
        T0_barl = cms.double(7.4),
        T0_endc = cms.double(3.1),
        T0_endcPresh = cms.double(1.2),
        W0 = cms.double(4.2),
        X0 = cms.double(0.89)
    ),
    reassignSeedCrysToClusterItSeeds = cms.bool(True)
)


process.multi5x5PreshowerClusterShape = cms.EDProducer("PreshowerClusterShapeProducer",
    PreshowerClusterShapeCollectionX = cms.string('multi5x5PreshowerXClustersShape'),
    PreshowerClusterShapeCollectionY = cms.string('multi5x5PreshowerYClustersShape'),
    debugLevel = cms.string('INFO'),
    endcapSClusterProducer = cms.InputTag("correctedMulti5x5SuperClustersWithPreshower"),
    preshPi0Nstrip = cms.int32(5),
    preshRecHitProducer = cms.InputTag("ecalPreshowerRecHit","EcalRecHitsES"),
    preshStripEnergyCut = cms.double(0.0)
)


process.multi5x5SuperClusters = cms.EDProducer("UnifiedSCCollectionProducer",
    bcCollection = cms.string('multi5x5EndcapBasicClusters'),
    bcCollectionUncleanOnly = cms.string('uncleanOnlyMulti5x5EndcapBasicClusters'),
    cleanBcCollection = cms.InputTag("multi5x5BasicClustersCleaned","multi5x5EndcapBasicClusters"),
    cleanScCollection = cms.InputTag("multi5x5SuperClustersCleaned","multi5x5EndcapSuperClusters"),
    scCollection = cms.string('multi5x5EndcapSuperClusters'),
    scCollectionUncleanOnly = cms.string('uncleanOnlyMulti5x5EndcapSuperClusters'),
    uncleanBcCollection = cms.InputTag("multi5x5BasicClustersUncleaned","multi5x5EndcapBasicClusters"),
    uncleanScCollection = cms.InputTag("multi5x5SuperClustersUncleaned","multi5x5EndcapSuperClusters")
)


process.multi5x5SuperClustersCleaned = cms.EDProducer("Multi5x5SuperClusterProducer",
    barrelClusterTag = cms.InputTag("multi5x5BasicClusters","multi5x5BarrelBasicClustersCleaned"),
    barrelEtaSearchRoad = cms.double(0.06),
    barrelPhiSearchRoad = cms.double(0.8),
    barrelSuperclusterCollection = cms.string('multi5x5BarrelSuperClusters'),
    bremRecoveryPset = cms.PSet(
        barrel = cms.PSet(
            cryMin = cms.int32(2),
            cryVec = cms.vint32(16, 13, 11, 10, 9, 
                8, 7, 6, 5, 4, 
                3),
            etVec = cms.vdouble(5.0, 10.0, 15.0, 20.0, 30.0, 
                40.0, 45.0, 55.0, 135.0, 195.0, 
                225.0)
        ),
        endcap = cms.PSet(
            a = cms.double(47.85),
            b = cms.double(108.8),
            c = cms.double(0.1201)
        )
    ),
    doBarrel = cms.bool(False),
    doEndcaps = cms.bool(True),
    dynamicPhiRoad = cms.bool(False),
    endcapClusterTag = cms.InputTag("multi5x5BasicClustersCleaned","multi5x5EndcapBasicClusters"),
    endcapEtaSearchRoad = cms.double(0.14),
    endcapPhiSearchRoad = cms.double(0.6),
    endcapSuperclusterCollection = cms.string('multi5x5EndcapSuperClusters'),
    seedTransverseEnergyThreshold = cms.double(1.0)
)


process.multi5x5SuperClustersUncleaned = cms.EDProducer("Multi5x5SuperClusterProducer",
    barrelClusterTag = cms.InputTag("multi5x5BasicClusters","multi5x5BarrelBasicClustersCleaned"),
    barrelEtaSearchRoad = cms.double(0.06),
    barrelPhiSearchRoad = cms.double(0.8),
    barrelSuperclusterCollection = cms.string('multi5x5BarrelSuperClusters'),
    bremRecoveryPset = cms.PSet(
        barrel = cms.PSet(
            cryMin = cms.int32(2),
            cryVec = cms.vint32(16, 13, 11, 10, 9, 
                8, 7, 6, 5, 4, 
                3),
            etVec = cms.vdouble(5.0, 10.0, 15.0, 20.0, 30.0, 
                40.0, 45.0, 55.0, 135.0, 195.0, 
                225.0)
        ),
        endcap = cms.PSet(
            a = cms.double(47.85),
            b = cms.double(108.8),
            c = cms.double(0.1201)
        )
    ),
    doBarrel = cms.bool(False),
    doEndcaps = cms.bool(True),
    dynamicPhiRoad = cms.bool(False),
    endcapClusterProducer = cms.string('multi5x5BasicClustersUncleaned'),
    endcapClusterTag = cms.InputTag("multi5x5BasicClustersCleaned","multi5x5EndcapBasicClusters"),
    endcapEtaSearchRoad = cms.double(0.14),
    endcapPhiSearchRoad = cms.double(0.6),
    endcapSuperclusterCollection = cms.string('multi5x5EndcapSuperClusters'),
    seedTransverseEnergyThreshold = cms.double(1.0)
)


process.multi5x5SuperClustersWithPreshower = cms.EDProducer("PreshowerPhiClusterProducer",
    assocSClusterCollection = cms.string(''),
    endcapSClusterProducer = cms.InputTag("multi5x5SuperClusters","multi5x5EndcapSuperClusters"),
    esPhiClusterDeltaEta = cms.double(0.15),
    esPhiClusterDeltaPhi = cms.double(0.12),
    esStripEnergyCut = cms.double(0.0),
    etThresh = cms.double(0.0),
    preshClusterCollectionX = cms.string('preshowerXClusters'),
    preshClusterCollectionY = cms.string('preshowerYClusters'),
    preshRecHitProducer = cms.InputTag("ecalPreshowerRecHit","EcalRecHitsES")
)


process.muonCSCDigis = cms.EDProducer("CSCDCCUnpacker",
    Debug = cms.untracked.bool(False),
    ErrorMask = cms.uint32(0),
    ExaminerMask = cms.uint32(535557110),
    FormatedEventDump = cms.untracked.bool(False),
    InputObjects = cms.InputTag("rawDataCollector"),
    PrintEventNumber = cms.untracked.bool(False),
    SuppressZeroLCT = cms.untracked.bool(True),
    UnpackStatusDigis = cms.bool(False),
    UseExaminer = cms.bool(True),
    UseFormatStatus = cms.bool(True),
    UseSelectiveUnpacking = cms.bool(True),
    VisualFEDInspect = cms.untracked.bool(False),
    VisualFEDShort = cms.untracked.bool(False),
    runDQM = cms.untracked.bool(False)
)


process.muonDTDigis = cms.EDProducer("DTUnpackingModule",
    dataType = cms.string('DDU'),
    dqmOnly = cms.bool(False),
    inputLabel = cms.InputTag("rawDataCollector"),
    maxFEDid = cms.untracked.int32(779),
    minFEDid = cms.untracked.int32(770),
    readOutParameters = cms.PSet(
        debug = cms.untracked.bool(False),
        localDAQ = cms.untracked.bool(False),
        performDataIntegrityMonitor = cms.untracked.bool(False),
        rosParameters = cms.PSet(
            debug = cms.untracked.bool(False),
            localDAQ = cms.untracked.bool(False),
            performDataIntegrityMonitor = cms.untracked.bool(False),
            readDDUIDfromDDU = cms.untracked.bool(True),
            readingDDU = cms.untracked.bool(True),
            writeSC = cms.untracked.bool(True)
        )
    ),
    useStandardFEDid = cms.bool(True)
)


process.muonMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(0.5),
    maxDeltaR = cms.double(0.5),
    mcPdgId = cms.vint32(13),
    mcStatus = cms.vint32(1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("muons")
)


process.muonRPCDigis = cms.EDProducer("RPCUnpackingModule",
    InputLabel = cms.InputTag("rawDataCollector"),
    doSynchro = cms.bool(True)
)


process.muonSelectionProducers = cms.EDProducer("MuonSelectionProducers",
    BeamSpotCollection = cms.InputTag("offlineBeamSpot"),
    chIsoVals = cms.InputTag("elPFIsoValueCharged03PFIdPFIso"),
    conversionCollection = cms.InputTag("allConversions"),
    emIsoVals = cms.InputTag("elPFIsoValueGamma03PFIdPFIso"),
    muonCollection = cms.InputTag("muons"),
    nhIsoVals = cms.InputTag("elPFIsoValueNeutral03PFIdPFIso"),
    rhoFastJet = cms.InputTag("kt6PFJetsForRhoCorrection","rho"),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.particleFlowClusterECAL = cms.EDProducer("CorrectedECALPFClusterProducer",
    energyCorrector = cms.PSet(
        algoName = cms.string('PFClusterEMEnergyCorrector'),
        applyCrackCorrections = cms.bool(False),
        applyMVACorrections = cms.bool(True),
        autoDetectBunchSpacing = cms.bool(True),
        maxPtForMVAEvaluation = cms.double(90.0),
        recHitsEBLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        recHitsEELabel = cms.InputTag("ecalRecHit","EcalRecHitsEE")
    ),
    inputECAL = cms.InputTag("particleFlowClusterECALUncorrected"),
    inputPS = cms.InputTag("particleFlowClusterPS"),
    minimumPSEnergy = cms.double(0.0)
)


process.particleFlowClusterECALUncorrected = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('ECAL_BARREL'),
            gatheringThreshold = cms.double(0.08),
            gatheringThresholdPt = cms.double(0.0)
        ), 
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                gatheringThreshold = cms.double(0.3),
                gatheringThresholdPt = cms.double(0.0)
            )),
        useCornerCells = cms.bool(True)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.08),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1),
            timeResolutionCalcBarrel = cms.PSet(
                constantTerm = cms.double(0.428192),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0510871),
                noiseTerm = cms.double(1.10889),
                noiseTermLowE = cms.double(1.31883),
                threshHighE = cms.double(5.0),
                threshLowE = cms.double(0.5)
            ),
            timeResolutionCalcEndcap = cms.PSet(
                constantTerm = cms.double(0.0),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0),
                noiseTerm = cms.double(5.72489999999),
                noiseTermLowE = cms.double(6.92683000001),
                threshHighE = cms.double(10.0),
                threshLowE = cms.double(1.0)
            )
        ),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.08),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(9),
            timeResolutionCalcBarrel = cms.PSet(
                constantTerm = cms.double(0.428192),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0510871),
                noiseTerm = cms.double(1.10889),
                noiseTermLowE = cms.double(1.31883),
                threshHighE = cms.double(5.0),
                threshLowE = cms.double(0.5)
            ),
            timeResolutionCalcEndcap = cms.PSet(
                constantTerm = cms.double(0.0),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0),
                noiseTerm = cms.double(5.72489999999),
                noiseTermLowE = cms.double(6.92683000001),
                threshHighE = cms.double(10.0),
                threshLowE = cms.double(1.0)
            )
        ),
        positionCalcForConvergence = cms.PSet(
            T0_EB = cms.double(7.4),
            T0_EE = cms.double(3.1),
            T0_ES = cms.double(1.2),
            W0 = cms.double(4.2),
            X0 = cms.double(0.89),
            algoName = cms.string('ECAL2DPositionCalcWithDepthCorr'),
            minAllowedNormalization = cms.double(0.0),
            minFractionInCalc = cms.double(0.0)
        ),
        recHitEnergyNorms = cms.VPSet(cms.PSet(
            detector = cms.string('ECAL_BARREL'),
            recHitEnergyNorm = cms.double(0.08)
        ), 
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                recHitEnergyNorm = cms.double(0.3)
            )),
        showerSigma = cms.double(1.5),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(
        T0_EB = cms.double(7.4),
        T0_EE = cms.double(3.1),
        T0_ES = cms.double(1.2),
        W0 = cms.double(4.2),
        X0 = cms.double(0.89),
        algoName = cms.string('ECAL2DPositionCalcWithDepthCorr'),
        minAllowedNormalization = cms.double(0.0),
        minFractionInCalc = cms.double(0.0)
    ),
    recHitCleaners = cms.VPSet(cms.PSet(
        algoName = cms.string('SpikeAndDoubleSpikeCleaner'),
        cleaningByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('ECAL_BARREL'),
            doubleSpikeS6S2 = cms.double(0.04),
            doubleSpikeThresh = cms.double(10.0),
            energyThresholdModifier = cms.double(2.0),
            fractionThresholdModifier = cms.double(3.0),
            minS4S1_a = cms.double(0.04),
            minS4S1_b = cms.double(-0.024),
            singleSpikeThresh = cms.double(4.0)
        ), 
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                doubleSpikeS6S2 = cms.double(-1.0),
                doubleSpikeThresh = cms.double(1000000000.0),
                energyThresholdModifier = cms.double(2.0),
                fractionThresholdModifier = cms.double(3.0),
                minS4S1_a = cms.double(0.02),
                minS4S1_b = cms.double(-0.0125),
                singleSpikeThresh = cms.double(15.0)
            ))
    )),
    recHitsSource = cms.InputTag("particleFlowRecHitECAL"),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(8),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('ECAL_ENDCAP'),
            seedingThreshold = cms.double(0.6),
            seedingThresholdPt = cms.double(0.15)
        ), 
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                seedingThreshold = cms.double(0.23),
                seedingThresholdPt = cms.double(0.0)
            ))
    )
)


process.particleFlowClusterHBHE = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('HCAL_BARREL1'),
            gatheringThreshold = cms.double(0.8),
            gatheringThresholdPt = cms.double(0.0)
        ), 
            cms.PSet(
                detector = cms.string('HCAL_ENDCAP'),
                gatheringThreshold = cms.double(0.8),
                gatheringThresholdPt = cms.double(0.0)
            )),
        useCornerCells = cms.bool(True)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.8),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        clusterTimeResFromSeed = cms.bool(False),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        maxNSigmaTime = cms.double(10.0),
        minChi2Prob = cms.double(0.0),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.8),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(5)
        ),
        recHitEnergyNorms = cms.VPSet(cms.PSet(
            detector = cms.string('HCAL_BARREL1'),
            recHitEnergyNorm = cms.double(0.8)
        ), 
            cms.PSet(
                detector = cms.string('HCAL_ENDCAP'),
                recHitEnergyNorm = cms.double(0.8)
            )),
        showerSigma = cms.double(10.0),
        stoppingTolerance = cms.double(1e-08),
        timeResolutionCalcBarrel = cms.PSet(
            constantTerm = cms.double(2.82),
            constantTermLowE = cms.double(4.24),
            corrTermLowE = cms.double(0.0),
            noiseTerm = cms.double(21.86),
            noiseTermLowE = cms.double(8),
            threshHighE = cms.double(15.0),
            threshLowE = cms.double(6.0)
        ),
        timeResolutionCalcEndcap = cms.PSet(
            constantTerm = cms.double(2.82),
            constantTermLowE = cms.double(4.24),
            corrTermLowE = cms.double(0.0),
            noiseTerm = cms.double(21.86),
            noiseTermLowE = cms.double(8),
            threshHighE = cms.double(15.0),
            threshLowE = cms.double(6.0)
        ),
        timeSigmaEB = cms.double(10.0),
        timeSigmaEE = cms.double(10.0)
    ),
    positionReCalc = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("particleFlowRecHitHBHE"),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(4),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('HCAL_BARREL1'),
            seedingThreshold = cms.double(1.0),
            seedingThresholdPt = cms.double(0.0)
        ), 
            cms.PSet(
                detector = cms.string('HCAL_ENDCAP'),
                seedingThreshold = cms.double(1.1),
                seedingThresholdPt = cms.double(0.0)
            ))
    )
)


process.particleFlowClusterHBHETimeSelected = cms.EDProducer("PFClusterTimeSelector",
    cuts = cms.VPSet(cms.PSet(
        depth = cms.double(1.0),
        endcap = cms.bool(False),
        maxEnergy = cms.double(1.0),
        maxTime = cms.double(30.0),
        minEnergy = cms.double(0.0),
        minTime = cms.double(-30.0)
    ), 
        cms.PSet(
            depth = cms.double(1.0),
            endcap = cms.bool(True),
            maxEnergy = cms.double(1.0),
            maxTime = cms.double(30.0),
            minEnergy = cms.double(0.0),
            minTime = cms.double(-30.0)
        ), 
        cms.PSet(
            depth = cms.double(2.0),
            endcap = cms.bool(False),
            maxEnergy = cms.double(1.0),
            maxTime = cms.double(30.0),
            minEnergy = cms.double(0.0),
            minTime = cms.double(-30.0)
        ), 
        cms.PSet(
            depth = cms.double(2.0),
            endcap = cms.bool(True),
            maxEnergy = cms.double(1.0),
            maxTime = cms.double(30.0),
            minEnergy = cms.double(0.0),
            minTime = cms.double(-30.0)
        ), 
        cms.PSet(
            depth = cms.double(3.0),
            endcap = cms.bool(False),
            maxEnergy = cms.double(1.0),
            maxTime = cms.double(30.0),
            minEnergy = cms.double(0.0),
            minTime = cms.double(-30.0)
        ), 
        cms.PSet(
            depth = cms.double(3.0),
            endcap = cms.bool(True),
            maxEnergy = cms.double(1.0),
            maxTime = cms.double(30.0),
            minEnergy = cms.double(0.0),
            minTime = cms.double(-30.0)
        ), 
        cms.PSet(
            depth = cms.double(1.0),
            endcap = cms.bool(False),
            maxEnergy = cms.double(2.0),
            maxTime = cms.double(15.0),
            minEnergy = cms.double(1.0),
            minTime = cms.double(-20.0)
        ), 
        cms.PSet(
            depth = cms.double(1.0),
            endcap = cms.bool(True),
            maxEnergy = cms.double(2.0),
            maxTime = cms.double(16.0),
            minEnergy = cms.double(1.0),
            minTime = cms.double(-20.0)
        ), 
        cms.PSet(
            depth = cms.double(2.0),
            endcap = cms.bool(False),
            maxEnergy = cms.double(2.0),
            maxTime = cms.double(15.0),
            minEnergy = cms.double(1.0),
            minTime = cms.double(-20.0)
        ), 
        cms.PSet(
            depth = cms.double(2.0),
            endcap = cms.bool(True),
            maxEnergy = cms.double(2.0),
            maxTime = cms.double(15.0),
            minEnergy = cms.double(1.0),
            minTime = cms.double(-20.0)
        ), 
        cms.PSet(
            depth = cms.double(3.0),
            endcap = cms.bool(False),
            maxEnergy = cms.double(2.0),
            maxTime = cms.double(15.0),
            minEnergy = cms.double(1.0),
            minTime = cms.double(-20.0)
        ), 
        cms.PSet(
            depth = cms.double(3.0),
            endcap = cms.bool(True),
            maxEnergy = cms.double(2.0),
            maxTime = cms.double(15.0),
            minEnergy = cms.double(1.0),
            minTime = cms.double(-20.0)
        ), 
        cms.PSet(
            depth = cms.double(1.0),
            endcap = cms.bool(False),
            maxEnergy = cms.double(5.0),
            maxTime = cms.double(25.0),
            minEnergy = cms.double(2.0),
            minTime = cms.double(-20.0)
        ), 
        cms.PSet(
            depth = cms.double(1.0),
            endcap = cms.bool(True),
            maxEnergy = cms.double(5.0),
            maxTime = cms.double(25.0),
            minEnergy = cms.double(2.0),
            minTime = cms.double(-20.0)
        ), 
        cms.PSet(
            depth = cms.double(2.0),
            endcap = cms.bool(False),
            maxEnergy = cms.double(5.0),
            maxTime = cms.double(25.0),
            minEnergy = cms.double(2.0),
            minTime = cms.double(-15.0)
        ), 
        cms.PSet(
            depth = cms.double(2.0),
            endcap = cms.bool(True),
            maxEnergy = cms.double(5.0),
            maxTime = cms.double(25.0),
            minEnergy = cms.double(2.0),
            minTime = cms.double(-15.0)
        ), 
        cms.PSet(
            depth = cms.double(3.0),
            endcap = cms.bool(False),
            maxEnergy = cms.double(5.0),
            maxTime = cms.double(25.0),
            minEnergy = cms.double(2.0),
            minTime = cms.double(-15.0)
        ), 
        cms.PSet(
            depth = cms.double(3.0),
            endcap = cms.bool(True),
            maxEnergy = cms.double(5.0),
            maxTime = cms.double(25.0),
            minEnergy = cms.double(2.0),
            minTime = cms.double(-15.0)
        ), 
        cms.PSet(
            depth = cms.double(1.0),
            endcap = cms.bool(False),
            maxEnergy = cms.double(9999999.0),
            maxTime = cms.double(20.0),
            minEnergy = cms.double(5.0),
            minTime = cms.double(-5)
        ), 
        cms.PSet(
            depth = cms.double(1.0),
            endcap = cms.bool(True),
            maxEnergy = cms.double(9999999.0),
            maxTime = cms.double(20.0),
            minEnergy = cms.double(5.0),
            minTime = cms.double(-5)
        ), 
        cms.PSet(
            depth = cms.double(2.0),
            endcap = cms.bool(False),
            maxEnergy = cms.double(9999999.0),
            maxTime = cms.double(20.0),
            minEnergy = cms.double(5.0),
            minTime = cms.double(-5)
        ), 
        cms.PSet(
            depth = cms.double(2.0),
            endcap = cms.bool(True),
            maxEnergy = cms.double(9999999.0),
            maxTime = cms.double(20.0),
            minEnergy = cms.double(5.0),
            minTime = cms.double(-5)
        ), 
        cms.PSet(
            depth = cms.double(3.0),
            endcap = cms.bool(False),
            maxEnergy = cms.double(9999999.0),
            maxTime = cms.double(20.0),
            minEnergy = cms.double(5.0),
            minTime = cms.double(-5)
        ), 
        cms.PSet(
            depth = cms.double(3.0),
            endcap = cms.bool(True),
            maxEnergy = cms.double(9999999.0),
            maxTime = cms.double(20.0),
            minEnergy = cms.double(5.0),
            minTime = cms.double(-5)
        )),
    src = cms.InputTag("particleFlowClusterHBHE")
)


process.particleFlowClusterHCAL = cms.EDProducer("PFMultiDepthClusterProducer",
    clustersSource = cms.InputTag("particleFlowClusterHBHE"),
    energyCorrector = cms.PSet(

    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('PFMultiDepthClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.8),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        minFractionToKeep = cms.double(1e-07),
        nSigmaEta = cms.double(2.0),
        nSigmaPhi = cms.double(2.0)
    ),
    positionReCalc = cms.PSet(

    )
)


process.particleFlowClusterHF = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('HF_EM'),
            gatheringThreshold = cms.double(0.8),
            gatheringThresholdPt = cms.double(0.0)
        ), 
            cms.PSet(
                detector = cms.string('HF_HAD'),
                gatheringThreshold = cms.double(0.8),
                gatheringThresholdPt = cms.double(0.0)
            )),
        useCornerCells = cms.bool(False)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.8),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.8),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(5)
        ),
        recHitEnergyNorms = cms.VPSet(cms.PSet(
            detector = cms.string('HF_EM'),
            recHitEnergyNorm = cms.double(0.8)
        ), 
            cms.PSet(
                detector = cms.string('HF_HAD'),
                recHitEnergyNorm = cms.double(0.8)
            )),
        showerSigma = cms.double(10.0),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(cms.PSet(
        algoName = cms.string('SpikeAndDoubleSpikeCleaner'),
        cleaningByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('HF_EM'),
            doubleSpikeS6S2 = cms.double(-1.0),
            doubleSpikeThresh = cms.double(1000000000.0),
            energyThresholdModifier = cms.double(1.0),
            fractionThresholdModifier = cms.double(1.0),
            minS4S1_a = cms.double(0.11),
            minS4S1_b = cms.double(-0.19),
            singleSpikeThresh = cms.double(80.0)
        ), 
            cms.PSet(
                detector = cms.string('HF_HAD'),
                doubleSpikeS6S2 = cms.double(-1.0),
                doubleSpikeThresh = cms.double(1000000000.0),
                energyThresholdModifier = cms.double(1.0),
                fractionThresholdModifier = cms.double(1.0),
                minS4S1_a = cms.double(0.045),
                minS4S1_b = cms.double(-0.08),
                singleSpikeThresh = cms.double(120.0)
            ))
    )),
    recHitsSource = cms.InputTag("particleFlowRecHitHF"),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(0),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('HF_EM'),
            seedingThreshold = cms.double(1.4),
            seedingThresholdPt = cms.double(0.0)
        ), 
            cms.PSet(
                detector = cms.string('HF_HAD'),
                seedingThreshold = cms.double(1.4),
                seedingThresholdPt = cms.double(0.0)
            ))
    )
)


process.particleFlowClusterHO = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('HCAL_BARREL2_RING0'),
            gatheringThreshold = cms.double(0.5),
            gatheringThresholdPt = cms.double(0.0)
        ), 
            cms.PSet(
                detector = cms.string('HCAL_BARREL2_RING1'),
                gatheringThreshold = cms.double(1.0),
                gatheringThresholdPt = cms.double(0.0)
            )),
        useCornerCells = cms.bool(True)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.5),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.5),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(5)
        ),
        recHitEnergyNorms = cms.VPSet(cms.PSet(
            detector = cms.string('HCAL_BARREL2_RING0'),
            recHitEnergyNorm = cms.double(0.5)
        ), 
            cms.PSet(
                detector = cms.string('HCAL_BARREL2_RING1'),
                recHitEnergyNorm = cms.double(1.0)
            )),
        showerSigma = cms.double(10.0),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("particleFlowRecHitHO"),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(4),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('HCAL_BARREL2_RING0'),
            seedingThreshold = cms.double(1.0),
            seedingThresholdPt = cms.double(0.0)
        ), 
            cms.PSet(
                detector = cms.string('HCAL_BARREL2_RING1'),
                seedingThreshold = cms.double(3.1),
                seedingThresholdPt = cms.double(0.0)
            ))
    )
)


process.particleFlowClusterPS = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('PS1'),
            gatheringThreshold = cms.double(6e-05),
            gatheringThresholdPt = cms.double(0.0)
        ), 
            cms.PSet(
                detector = cms.string('PS2'),
                gatheringThreshold = cms.double(6e-05),
                gatheringThresholdPt = cms.double(0.0)
            )),
        useCornerCells = cms.bool(False)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(6e-05),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        recHitEnergyNorms = cms.VPSet(cms.PSet(
            detector = cms.string('PS1'),
            recHitEnergyNorm = cms.double(6e-05)
        ), 
            cms.PSet(
                detector = cms.string('PS2'),
                recHitEnergyNorm = cms.double(6e-05)
            )),
        showerSigma = cms.double(0.3),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("particleFlowRecHitPS"),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(4),
        thresholdsByDetector = cms.VPSet(cms.PSet(
            detector = cms.string('PS1'),
            seedingThreshold = cms.double(0.00012),
            seedingThresholdPt = cms.double(0.0)
        ), 
            cms.PSet(
                detector = cms.string('PS2'),
                seedingThreshold = cms.double(0.00012),
                seedingThresholdPt = cms.double(0.0)
            ))
    )
)


process.particleFlowRecHitECAL = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        barrel = cms.PSet(

        ),
        endcap = cms.PSet(

        ),
        name = cms.string('PFRecHitECALNavigator')
    ),
    producers = cms.VPSet(cms.PSet(
        name = cms.string('PFEBRecHitCreator'),
        qualityTests = cms.VPSet(cms.PSet(
            name = cms.string('PFRecHitQTestThreshold'),
            threshold = cms.double(0.08)
        ), 
            cms.PSet(
                cleaningThreshold = cms.double(2.0),
                name = cms.string('PFRecHitQTestECAL'),
                skipTTRecoveredHits = cms.bool(True),
                timingCleaning = cms.bool(True),
                topologicalCleaning = cms.bool(True)
            )),
        src = cms.InputTag("ecalRecHit","EcalRecHitsEB")
    ), 
        cms.PSet(
            name = cms.string('PFEERecHitCreator'),
            qualityTests = cms.VPSet(cms.PSet(
                name = cms.string('PFRecHitQTestThreshold'),
                threshold = cms.double(0.3)
            ), 
                cms.PSet(
                    cleaningThreshold = cms.double(2.0),
                    name = cms.string('PFRecHitQTestECAL'),
                    skipTTRecoveredHits = cms.bool(True),
                    timingCleaning = cms.bool(True),
                    topologicalCleaning = cms.bool(True)
                )),
            src = cms.InputTag("ecalRecHit","EcalRecHitsEE")
        ))
)


process.particleFlowRecHitHBHE = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        name = cms.string('PFRecHitHCALNavigator'),
        sigmaCut = cms.double(4.0),
        timeResolutionCalc = cms.PSet(
            constantTerm = cms.double(1.92),
            constantTermLowE = cms.double(6.0),
            corrTermLowE = cms.double(0.0),
            noiseTerm = cms.double(8.64),
            noiseTermLowE = cms.double(0.0),
            threshHighE = cms.double(8.0),
            threshLowE = cms.double(2.0)
        )
    ),
    producers = cms.VPSet(cms.PSet(
        name = cms.string('PFHBHERecHitCreator'),
        qualityTests = cms.VPSet(cms.PSet(
            name = cms.string('PFRecHitQTestThreshold'),
            threshold = cms.double(0.8)
        ), 
            cms.PSet(
                cleaningThresholds = cms.vdouble(0.0),
                flags = cms.vstring('Standard'),
                maxSeverities = cms.vint32(11),
                name = cms.string('PFRecHitQTestHCALChannel')
            )),
        src = cms.InputTag("hbhereco")
    ))
)


process.particleFlowRecHitHF = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        barrel = cms.PSet(

        ),
        endcap = cms.PSet(

        ),
        name = cms.string('PFRecHitHCALNavigator')
    ),
    producers = cms.VPSet(cms.PSet(
        EMDepthCorrection = cms.double(22.0),
        HADDepthCorrection = cms.double(25.0),
        HFCalib29 = cms.double(1.07),
        LongFibre_Cut = cms.double(120.0),
        LongFibre_Fraction = cms.double(0.1),
        ShortFibre_Cut = cms.double(60.0),
        ShortFibre_Fraction = cms.double(0.01),
        name = cms.string('PFHFRecHitCreator'),
        qualityTests = cms.VPSet(cms.PSet(
            cleaningThresholds = cms.vdouble(0.0, 120.0, 60.0, 30.0),
            flags = cms.vstring('Standard', 
                'HFLong', 
                'HFShort', 
                'HFDigi'),
            maxSeverities = cms.vint32(11, 9, 9, 9),
            name = cms.string('PFRecHitQTestHCALChannel')
        ), 
            cms.PSet(
                cuts = cms.VPSet(cms.PSet(
                    depth = cms.int32(1),
                    threshold = cms.double(1.2)
                ), 
                    cms.PSet(
                        depth = cms.int32(2),
                        threshold = cms.double(1.8)
                    )),
                name = cms.string('PFRecHitQTestHCALThresholdVsDepth')
            )),
        src = cms.InputTag("hfreco"),
        thresh_HF = cms.double(0.4)
    ))
)


process.particleFlowRecHitHO = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        name = cms.string('PFRecHitHCALNavigator')
    ),
    producers = cms.VPSet(cms.PSet(
        name = cms.string('PFHORecHitCreator'),
        qualityTests = cms.VPSet(cms.PSet(
            name = cms.string('PFRecHitQTestHOThreshold'),
            threshold_ring0 = cms.double(0.4),
            threshold_ring12 = cms.double(1.0)
        ), 
            cms.PSet(
                cleaningThresholds = cms.vdouble(0.0),
                flags = cms.vstring('Standard'),
                maxSeverities = cms.vint32(11),
                name = cms.string('PFRecHitQTestHCALChannel')
            )),
        src = cms.InputTag("horeco")
    ))
)


process.particleFlowRecHitPS = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        name = cms.string('PFRecHitPreshowerNavigator')
    ),
    producers = cms.VPSet(cms.PSet(
        name = cms.string('PFPSRecHitCreator'),
        qualityTests = cms.VPSet(cms.PSet(
            name = cms.string('PFRecHitQTestThreshold'),
            threshold = cms.double(0.0)
        ), 
            cms.PSet(
                cleaningThreshold = cms.double(0.0),
                name = cms.string('PFRecHitQTestES'),
                topologicalCleaning = cms.bool(True)
            )),
        src = cms.InputTag("ecalPreshowerRecHit","EcalRecHitsES")
    ))
)


process.particleFlowSuperClusterECAL = cms.EDProducer("PFECALSuperClusterProducer",
    BeamSpot = cms.InputTag("offlineBeamSpot"),
    ClusteringType = cms.string('Mustache'),
    ESAssociation = cms.InputTag("particleFlowClusterECAL"),
    EnergyWeight = cms.string('Raw'),
    PFBasicClusterCollectionBarrel = cms.string('particleFlowBasicClusterECALBarrel'),
    PFBasicClusterCollectionEndcap = cms.string('particleFlowBasicClusterECALEndcap'),
    PFBasicClusterCollectionPreshower = cms.string('particleFlowBasicClusterECALPreshower'),
    PFClusters = cms.InputTag("particleFlowClusterECAL"),
    PFSuperClusterCollectionBarrel = cms.string('particleFlowSuperClusterECALBarrel'),
    PFSuperClusterCollectionEndcap = cms.string('particleFlowSuperClusterECALEndcap'),
    PFSuperClusterCollectionEndcapWithPreshower = cms.string('particleFlowSuperClusterECALEndcapWithPreshower'),
    applyCrackCorrections = cms.bool(False),
    doSatelliteClusterMerge = cms.bool(False),
    etawidth_SuperClusterBarrel = cms.double(0.04),
    etawidth_SuperClusterEndcap = cms.double(0.04),
    phiwidth_SuperClusterBarrel = cms.double(0.6),
    phiwidth_SuperClusterEndcap = cms.double(0.6),
    regressionConfig = cms.PSet(
        ecalRecHitsEB = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        ecalRecHitsEE = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        regressionKeyEB = cms.string('pfscecal_EBCorrection_offline_v2'),
        regressionKeyEE = cms.string('pfscecal_EECorrection_offline_v2'),
        uncertaintyKeyEB = cms.string('pfscecal_EBUncertainty_offline_v2'),
        uncertaintyKeyEE = cms.string('pfscecal_EEUncertainty_offline_v2'),
        vertexCollection = cms.InputTag("offlinePrimaryVertices")
    ),
    satelliteClusterSeedThreshold = cms.double(50.0),
    satelliteMajorityFraction = cms.double(0.5),
    seedThresholdIsET = cms.bool(True),
    thresh_PFClusterBarrel = cms.double(0.0),
    thresh_PFClusterES = cms.double(0.0),
    thresh_PFClusterEndcap = cms.double(0.0),
    thresh_PFClusterSeedBarrel = cms.double(1.0),
    thresh_PFClusterSeedEndcap = cms.double(1.0),
    thresh_SCEt = cms.double(4.0),
    useDynamicDPhiWindow = cms.bool(True),
    useRegression = cms.bool(True),
    use_preshower = cms.bool(True),
    verbose = cms.untracked.bool(False)
)


process.particleFlowSuperClusterECALBox = cms.EDProducer("PFECALSuperClusterProducer",
    BeamSpot = cms.InputTag("offlineBeamSpot"),
    ClusteringType = cms.string('Box'),
    ESAssociation = cms.InputTag("particleFlowClusterECAL"),
    EnergyWeight = cms.string('Raw'),
    PFBasicClusterCollectionBarrel = cms.string('particleFlowBasicClusterECALBarrel'),
    PFBasicClusterCollectionEndcap = cms.string('particleFlowBasicClusterECALEndcap'),
    PFBasicClusterCollectionPreshower = cms.string('particleFlowBasicClusterECALPreshower'),
    PFClusters = cms.InputTag("particleFlowClusterECAL"),
    PFSuperClusterCollectionBarrel = cms.string('particleFlowSuperClusterECALBarrel'),
    PFSuperClusterCollectionEndcap = cms.string('particleFlowSuperClusterECALEndcap'),
    PFSuperClusterCollectionEndcapWithPreshower = cms.string('particleFlowSuperClusterECALEndcapWithPreshower'),
    applyCrackCorrections = cms.bool(False),
    doSatelliteClusterMerge = cms.bool(False),
    etawidth_SuperClusterBarrel = cms.double(0.04),
    etawidth_SuperClusterEndcap = cms.double(0.04),
    phiwidth_SuperClusterBarrel = cms.double(0.28),
    phiwidth_SuperClusterEndcap = cms.double(0.28),
    regressionConfig = cms.PSet(
        ecalRecHitsEB = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        ecalRecHitsEE = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        regressionKeyEB = cms.string('pfscecal_EBCorrection_offline_v2'),
        regressionKeyEE = cms.string('pfscecal_EECorrection_offline_v2'),
        uncertaintyKeyEB = cms.string('pfscecal_EBUncertainty_offline_v2'),
        uncertaintyKeyEE = cms.string('pfscecal_EEUncertainty_offline_v2'),
        vertexCollection = cms.InputTag("offlinePrimaryVertices")
    ),
    satelliteClusterSeedThreshold = cms.double(50.0),
    satelliteMajorityFraction = cms.double(0.5),
    seedThresholdIsET = cms.bool(True),
    thresh_PFClusterBarrel = cms.double(0.5),
    thresh_PFClusterES = cms.double(0.0),
    thresh_PFClusterEndcap = cms.double(0.5),
    thresh_PFClusterSeedBarrel = cms.double(3.0),
    thresh_PFClusterSeedEndcap = cms.double(5.0),
    thresh_SCEt = cms.double(4.0),
    useDynamicDPhiWindow = cms.bool(False),
    useRegression = cms.bool(False),
    use_preshower = cms.bool(True),
    verbose = cms.untracked.bool(False)
)


process.particleFlowSuperClusterECALMustache = cms.EDProducer("PFECALSuperClusterProducer",
    BeamSpot = cms.InputTag("offlineBeamSpot"),
    ClusteringType = cms.string('Mustache'),
    ESAssociation = cms.InputTag("particleFlowClusterECAL"),
    EnergyWeight = cms.string('Raw'),
    PFBasicClusterCollectionBarrel = cms.string('particleFlowBasicClusterECALBarrel'),
    PFBasicClusterCollectionEndcap = cms.string('particleFlowBasicClusterECALEndcap'),
    PFBasicClusterCollectionPreshower = cms.string('particleFlowBasicClusterECALPreshower'),
    PFClusters = cms.InputTag("particleFlowClusterECAL"),
    PFSuperClusterCollectionBarrel = cms.string('particleFlowSuperClusterECALBarrel'),
    PFSuperClusterCollectionEndcap = cms.string('particleFlowSuperClusterECALEndcap'),
    PFSuperClusterCollectionEndcapWithPreshower = cms.string('particleFlowSuperClusterECALEndcapWithPreshower'),
    applyCrackCorrections = cms.bool(False),
    doSatelliteClusterMerge = cms.bool(False),
    etawidth_SuperClusterBarrel = cms.double(0.04),
    etawidth_SuperClusterEndcap = cms.double(0.04),
    phiwidth_SuperClusterBarrel = cms.double(0.6),
    phiwidth_SuperClusterEndcap = cms.double(0.6),
    regressionConfig = cms.PSet(
        ecalRecHitsEB = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        ecalRecHitsEE = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        regressionKeyEB = cms.string('pfscecal_EBCorrection_offline_v2'),
        regressionKeyEE = cms.string('pfscecal_EECorrection_offline_v2'),
        uncertaintyKeyEB = cms.string('pfscecal_EBUncertainty_offline_v2'),
        uncertaintyKeyEE = cms.string('pfscecal_EEUncertainty_offline_v2'),
        vertexCollection = cms.InputTag("offlinePrimaryVertices")
    ),
    satelliteClusterSeedThreshold = cms.double(50.0),
    satelliteMajorityFraction = cms.double(0.5),
    seedThresholdIsET = cms.bool(True),
    thresh_PFClusterBarrel = cms.double(0.0),
    thresh_PFClusterES = cms.double(0.0),
    thresh_PFClusterEndcap = cms.double(0.0),
    thresh_PFClusterSeedBarrel = cms.double(1.0),
    thresh_PFClusterSeedEndcap = cms.double(1.0),
    thresh_SCEt = cms.double(4.0),
    useDynamicDPhiWindow = cms.bool(True),
    useRegression = cms.bool(True),
    use_preshower = cms.bool(True),
    verbose = cms.untracked.bool(False)
)


process.patElectrons = cms.EDProducer("PATElectronProducer",
    addEfficiencies = cms.bool(False),
    addElectronID = cms.bool(False),
    addGenMatch = cms.bool(True),
    addPFClusterIso = cms.bool(False),
    addResolutions = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    efficiencies = cms.PSet(

    ),
    electronIDSources = cms.PSet(
        eidLoose = cms.InputTag("eidLoose"),
        eidRobustHighEnergy = cms.InputTag("eidRobustHighEnergy"),
        eidRobustLoose = cms.InputTag("eidRobustLoose"),
        eidRobustTight = cms.InputTag("eidRobustTight"),
        eidTight = cms.InputTag("eidTight")
    ),
    electronSource = cms.InputTag("gedGsfElectrons"),
    embedBasicClusters = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedGsfElectronCore = cms.bool(True),
    embedGsfTrack = cms.bool(True),
    embedHighLevelSelection = cms.bool(True),
    embedPFCandidate = cms.bool(True),
    embedPflowBasicClusters = cms.bool(True),
    embedPflowPreshowerClusters = cms.bool(True),
    embedPflowSuperCluster = cms.bool(True),
    embedPreshowerClusters = cms.bool(True),
    embedRecHits = cms.bool(True),
    embedSeedCluster = cms.bool(True),
    embedSuperCluster = cms.bool(True),
    embedTrack = cms.bool(False),
    genParticleMatch = cms.InputTag("electronMatch"),
    isoDeposits = cms.PSet(

    ),
    pfCandidateMap = cms.InputTag("particleFlow","electrons"),
    pfElectronSource = cms.InputTag("particleFlow"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    reducedBarrelRecHitCollection = cms.InputTag("alCaIsolatedElectrons","alcaBarrelHits"),
    reducedEndcapRecHitCollection = cms.InputTag("alCaIsolatedElectrons","alcaEndcapHits"),
    resolutions = cms.PSet(

    ),
    useParticleFlow = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patMuons = cms.EDProducer("PATMuonProducer",
    addEfficiencies = cms.bool(False),
    addGenMatch = cms.bool(True),
    addResolutions = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    caloMETMuonCorrs = cms.InputTag("muonMETValueMapProducer","muCorrData"),
    efficiencies = cms.PSet(

    ),
    embedCaloMETMuonCorrs = cms.bool(True),
    embedCombinedMuon = cms.bool(True),
    embedDytMuon = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedHighLevelSelection = cms.bool(True),
    embedMuonBestTrack = cms.bool(True),
    embedPFCandidate = cms.bool(True),
    embedPfEcalEnergy = cms.bool(True),
    embedPickyMuon = cms.bool(True),
    embedStandAloneMuon = cms.bool(True),
    embedTcMETMuonCorrs = cms.bool(False),
    embedTpfmsMuon = cms.bool(True),
    embedTrack = cms.bool(False),
    embedTunePMuonBestTrack = cms.bool(True),
    forceBestTrackEmbedding = cms.bool(False),
    genParticleMatch = cms.InputTag("muonMatch"),
    isoDeposits = cms.PSet(

    ),
    muonSource = cms.InputTag("muons"),
    pfMuonSource = cms.InputTag("particleFlow"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    resolutions = cms.PSet(

    ),
    tcMETMuonCorrs = cms.InputTag("muonTCMETValueMapProducer","muCorrData"),
    useParticleFlow = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patPhotons = cms.EDProducer("PATPhotonProducer",
    addEfficiencies = cms.bool(False),
    addGenMatch = cms.bool(True),
    addPFClusterIso = cms.bool(False),
    addPhotonID = cms.bool(True),
    addResolutions = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    efficiencies = cms.PSet(

    ),
    electronSource = cms.InputTag("gedGsfElectrons"),
    embedBasicClusters = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedPreshowerClusters = cms.bool(True),
    embedRecHits = cms.bool(True),
    embedSeedCluster = cms.bool(True),
    embedSuperCluster = cms.bool(True),
    genParticleMatch = cms.InputTag("photonMatch"),
    isoDeposits = cms.PSet(

    ),
    photonIDSources = cms.PSet(
        fiducial = cms.InputTag("phoSelectionProducers","fiducial"),
        loose = cms.InputTag("phoSelectionProducers","loose"),
        loose25nsRun2 = cms.InputTag("phoSelectionProducers","loose25nsRun2"),
        medium = cms.InputTag("phoSelectionProducers","medium"),
        medium25nsRun2 = cms.InputTag("phoSelectionProducers","medium25nsRun2"),
        tight = cms.InputTag("phoSelectionProducers","tight"),
        tight25nsRun2 = cms.InputTag("phoSelectionProducers","tight25nsRun2")
    ),
    photonSource = cms.InputTag("gedPhotons"),
    reducedBarrelRecHitCollection = cms.InputTag("alCaIsolatedElectrons","alcaBarrelHits"),
    reducedEndcapRecHitCollection = cms.InputTag("alCaIsolatedElectrons","alcaEndcapHits"),
    resolutions = cms.PSet(

    ),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patTrigger = cms.EDProducer("PATTriggerProducer",
    l1GtReadoutRecordInputTag = cms.InputTag("gtDigis"),
    l1GtRecordInputTag = cms.InputTag("gtDigis"),
    l1GtTriggerMenuLiteInputTag = cms.InputTag("gtDigis"),
    l1tAlgBlkInputTag = cms.InputTag("gtStage2Digis"),
    l1tExtBlkInputTag = cms.InputTag("gtStage2Digis"),
    onlyStandAlone = cms.bool(False),
    processName = cms.string('HLT')
)


process.patTriggerEvent = cms.EDProducer("PATTriggerEventProducer",
    patTriggerMatches = cms.VInputTag("PatElectronsTriggerMatch"),
    processName = cms.string('HLT')
)


process.phoSelectionProducers = cms.EDProducer("PhoSelectionProducers",
    BeamSpotCollection = cms.InputTag("offlineBeamSpot"),
    chIsoVals = cms.InputTag("phPFIsoValueCharged03PFIdPFIso"),
    conversionCollection = cms.InputTag("allConversions"),
    emIsoVals = cms.InputTag("phPFIsoValueGamma03PFIdPFIso"),
    nhIsoVals = cms.InputTag("phPFIsoValueNeutral03PFIdPFIso"),
    photonCollection = cms.InputTag("gedPhotons"),
    rhoFastJet = cms.InputTag("kt6PFJetsForRhoCorrection","rho"),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.photonIDValueMapProducer = cms.EDProducer("PhotonIDValueMapProducer",
    ebReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    ebReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    eeReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    eeReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEERecHits"),
    esReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsES"),
    esReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedESRecHits"),
    particleBasedIsolation = cms.InputTag("particleBasedIsolation","gedPhotons"),
    pfCandidates = cms.InputTag("particleFlow"),
    pfCandidatesMiniAOD = cms.InputTag("packedPFCandidates"),
    src = cms.InputTag("gedPhotons"),
    srcMiniAOD = cms.InputTag("slimmedPhotons","","@skipCurrentProcess"),
    vertices = cms.InputTag("offlinePrimaryVertices"),
    verticesMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.photonMVAValueMapProducer = cms.EDProducer("PhotonMVAValueMapProducer",
    mvaConfigurations = cms.VPSet(cms.PSet(
        esEffSigmaRRMap = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
        full5x5E1x3Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E1x3"),
        full5x5E2x2Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x2"),
        full5x5E2x5MaxMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x5Max"),
        full5x5E5x5Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E5x5"),
        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
        full5x5SigmaIEtaIPhiMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
        mvaName = cms.string('PhotonMVAEstimatorRun2Phys14NonTrig'),
        mvaTag = cms.string('25nsV1'),
        phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
        phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
        phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
        rho = cms.InputTag("fixedGridRhoFastjetAll"),
        useValueMaps = cms.bool(True),
        weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/PHYS14/photon_general_MVA_phys14_pu20bx25_EB_V1.weights.xml', 
            'RecoEgamma/PhotonIdentification/data/PHYS14/photon_general_MVA_phys14_pu20bx25_EE_V1.weights.xml')
    ), 
        cms.PSet(
            esEffSigmaRRMap = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
            full5x5E1x3Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E1x3"),
            full5x5E2x2Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x2"),
            full5x5E2x5MaxMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x5Max"),
            full5x5E5x5Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E5x5"),
            full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
            full5x5SigmaIEtaIPhiMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
            mvaName = cms.string('PhotonMVAEstimatorRun2Spring15NonTrig'),
            mvaTag = cms.string('50nsV1'),
            phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
            phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
            phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
            rho = cms.InputTag("fixedGridRhoFastjetAll"),
            useValueMaps = cms.bool(True),
            weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_50ns_EB_V1.weights.xml', 
                'RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_50ns_EE_V1.weights.xml')
        ), 
        cms.PSet(
            esEffSigmaRRMap = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
            full5x5E1x3Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E1x3"),
            full5x5E2x2Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x2"),
            full5x5E2x5MaxMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x5Max"),
            full5x5E5x5Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E5x5"),
            full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
            full5x5SigmaIEtaIPhiMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
            mvaName = cms.string('PhotonMVAEstimatorRun2Spring15NonTrig'),
            mvaTag = cms.string('50nsV2'),
            phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
            phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
            phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
            rho = cms.InputTag("fixedGridRhoFastjetAll"),
            useValueMaps = cms.bool(True),
            weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_50ns_EB_V2.weights.xml', 
                'RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_50ns_EE_V2.weights.xml')
        ), 
        cms.PSet(
            esEffSigmaRRMap = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
            full5x5E1x3Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E1x3"),
            full5x5E2x2Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x2"),
            full5x5E2x5MaxMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x5Max"),
            full5x5E5x5Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E5x5"),
            full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
            full5x5SigmaIEtaIPhiMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
            mvaName = cms.string('PhotonMVAEstimatorRun2Spring15NonTrig'),
            mvaTag = cms.string('25nsV2'),
            phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
            phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
            phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
            rho = cms.InputTag("fixedGridRhoFastjetAll"),
            useValueMaps = cms.bool(True),
            weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_25ns_EB_V2.weights.xml', 
                'RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_25ns_EE_V2.weights.xml')
        ), 
        cms.PSet(
            esEffSigmaRRMap = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
            full5x5E1x3Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E1x3"),
            full5x5E2x2Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x2"),
            full5x5E2x5MaxMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x5Max"),
            full5x5E5x5Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E5x5"),
            full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
            full5x5SigmaIEtaIPhiMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
            mvaName = cms.string('PhotonMVAEstimatorRun2Spring15NonTrig'),
            mvaTag = cms.string('50nsV2p1'),
            phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
            phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
            phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
            rho = cms.InputTag("fixedGridRhoFastjetAll"),
            useValueMaps = cms.bool(False),
            weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_50ns_EB_V2.weights.xml', 
                'RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_50ns_EE_V2.weights.xml')
        ), 
        cms.PSet(
            esEffSigmaRRMap = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
            full5x5E1x3Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E1x3"),
            full5x5E2x2Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x2"),
            full5x5E2x5MaxMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x5Max"),
            full5x5E5x5Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E5x5"),
            full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
            full5x5SigmaIEtaIPhiMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
            mvaName = cms.string('PhotonMVAEstimatorRun2Spring15NonTrig'),
            mvaTag = cms.string('25nsV2p1'),
            phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
            phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
            phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
            rho = cms.InputTag("fixedGridRhoFastjetAll"),
            useValueMaps = cms.bool(False),
            weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_25ns_EB_V2.weights.xml', 
                'RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_25ns_EE_V2.weights.xml')
        )),
    src = cms.InputTag("gedPhotons"),
    srcMiniAOD = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
)


process.photonMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(1.0),
    maxDeltaR = cms.double(0.2),
    mcPdgId = cms.vint32(22),
    mcStatus = cms.vint32(1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("gedPhotons")
)


process.randomEngineStateProducer = cms.EDProducer("RandomEngineStateProducer")


process.reducedEcalRecHitsEB = cms.EDProducer("ReducedRecHitCollectionProducer",
    interestingDetIdCollections = cms.VInputTag(cms.InputTag("interestingEcalDetIdEB"), cms.InputTag("interestingEcalDetIdEBU"), cms.InputTag("interestingEcalDetIdPFEB"), cms.InputTag("interestingEcalDetIdRefinedEB"), cms.InputTag("interestingGedEleIsoDetIdEB"), 
        cms.InputTag("interestingGedGamIsoDetIdEB"), cms.InputTag("interestingGamIsoDetIdEB"), cms.InputTag("muonEcalDetIds"), cms.InputTag("interestingTrackEcalDetIds")),
    recHitsLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    reducedHitsCollection = cms.string('')
)


process.reducedEcalRecHitsEE = cms.EDProducer("ReducedRecHitCollectionProducer",
    interestingDetIdCollections = cms.VInputTag(cms.InputTag("interestingEcalDetIdEE"), cms.InputTag("interestingEcalDetIdPFEE"), cms.InputTag("interestingEcalDetIdRefinedEE"), cms.InputTag("interestingGedEleIsoDetIdEE"), cms.InputTag("interestingGedGamIsoDetIdEE"), 
        cms.InputTag("interestingGamIsoDetIdEE"), cms.InputTag("muonEcalDetIds"), cms.InputTag("interestingTrackEcalDetIds")),
    recHitsLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    reducedHitsCollection = cms.string('')
)


process.reducedEcalRecHitsES = cms.EDProducer("ReducedESRecHitCollectionProducer",
    EcalRecHitCollectionES = cms.InputTag("ecalPreshowerRecHit","EcalRecHitsES"),
    EndcapSuperClusterCollection = cms.InputTag("correctedMulti5x5SuperClustersWithPreshower"),
    OutputLabel_ES = cms.string(''),
    interestingDetIds = cms.VInputTag(cms.InputTag("interestingEcalDetIdPFES"), cms.InputTag("interestingEcalDetIdRefinedES")),
    interestingDetIdsNotToClean = cms.VInputTag(cms.InputTag("interestingGedEgammaIsoESDetId")),
    scEtThreshold = cms.double(15)
)


process.reducedHcalRecHits = cms.EDProducer("HcalHitSelection",
    hbheTag = cms.InputTag("hbhereco"),
    hfTag = cms.InputTag("hfreco"),
    hoSeverityLevel = cms.int32(13),
    hoTag = cms.InputTag("horeco"),
    interestingDetIds = cms.VInputTag(cms.InputTag("interestingGedEgammaIsoHCALDetId"))
)


process.scalersRawToDigi = cms.EDProducer("ScalersRawToDigi",
    scalersInputTag = cms.InputTag("rawDataCollector")
)


process.selectDigi = cms.EDProducer("EcalDigiSelector",
    EcalEBDigiTag = cms.InputTag("ecalDigis","ebDigis"),
    EcalEBRecHitTag = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    EcalEEDigiTag = cms.InputTag("ecalDigis","eeDigis"),
    EcalEERecHitTag = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    barrelSuperClusterProducer = cms.InputTag("uncleanedHybridSuperClusters"),
    cluster_pt_thresh = cms.double(10.0),
    endcapSuperClusterProducer = cms.InputTag("correctedMulti5x5SuperClustersWithPreshower"),
    nclus_sel = cms.int32(2),
    selectedEcalEBDigiCollection = cms.string('selectedEcalEBDigiCollection'),
    selectedEcalEEDigiCollection = cms.string('selectedEcalEEDigiCollection'),
    single_cluster_thresh = cms.double(15.0)
)


process.siPixelDigis = cms.EDProducer("SiPixelRawToDigi",
    CablingMapLabel = cms.string(''),
    ErrorList = cms.vint32(29),
    IncludeErrors = cms.bool(True),
    InputLabel = cms.InputTag("rawDataCollector"),
    Regions = cms.PSet(

    ),
    Timing = cms.untracked.bool(False),
    UsePhase1 = cms.bool(False),
    UsePilotBlade = cms.bool(False),
    UseQualityInfo = cms.bool(False),
    UserErrorList = cms.vint32(40)
)


process.siStripDigis = cms.EDProducer("SiStripRawToDigiModule",
    AppendedBytes = cms.int32(0),
    DoAPVEmulatorCheck = cms.bool(False),
    DoAllCorruptBufferChecks = cms.bool(False),
    ErrorThreshold = cms.uint32(7174),
    LegacyUnpacker = cms.bool(False),
    MarkModulesOnMissingFeds = cms.bool(True),
    ProductLabel = cms.InputTag("rawDataCollector"),
    TriggerFedId = cms.int32(0),
    UnpackBadChannels = cms.bool(False),
    UnpackCommonModeValues = cms.bool(False),
    UseDaqRegister = cms.bool(False),
    UseFedKey = cms.bool(False)
)


process.simEcalTriggerPrimitiveDigis = cms.EDProducer("EcalTrigPrimProducer",
    BarrelOnly = cms.bool(False),
    Debug = cms.bool(False),
    Famos = cms.bool(False),
    InstanceEB = cms.string(''),
    InstanceEE = cms.string(''),
    Label = cms.string('simEcalUnsuppressedDigis'),
    TcpOutput = cms.bool(False),
    binOfMaximum = cms.int32(6)
)


process.slimmedECALELFElectrons = cms.EDProducer("PATElectronSlimmer",
    dropBasicClusters = cms.string('0'),
    dropClassifications = cms.string('pt < 5'),
    dropCorrections = cms.string('pt < 5'),
    dropExtrapolations = cms.string('pt < 5'),
    dropIsolations = cms.string('pt < 5'),
    dropPFlowClusters = cms.string('0'),
    dropPreshowerClusters = cms.string('0'),
    dropRecHits = cms.string('0'),
    dropSeedCluster = cms.string('0'),
    dropShapes = cms.string('pt < 5'),
    dropSuperCluster = cms.string('0'),
    linkToPackedPFCandidates = cms.bool(False),
    modifierConfig = cms.PSet(
        modifications = cms.VPSet(cms.PSet(
            electron_config = cms.PSet(
                WP70PU = cms.InputTag("eleSelectionProducers","WP70PU"),
                WP80PU = cms.InputTag("eleSelectionProducers","WP80PU"),
                WP90PU = cms.InputTag("eleSelectionProducers","WP90PU"),
                electronSrc = cms.InputTag("slimmedElectrons"),
                energySCEleMust = cms.InputTag("eleNewEnergiesProducer","energySCEleMust"),
                energySCEleMustVar = cms.InputTag("eleNewEnergiesProducer","energySCEleMustVar"),
                energySCElePho = cms.InputTag("eleNewEnergiesProducer","energySCElePho"),
                energySCElePhoVar = cms.InputTag("eleNewEnergiesProducer","energySCElePhoVar"),
                fiducial = cms.InputTag("eleSelectionProducers","fiducial"),
                loose = cms.InputTag("eleSelectionProducers","loose"),
                loose25nsRun2 = cms.InputTag("eleSelectionProducers","loose25nsRun2"),
                loose50nsRun2 = cms.InputTag("eleSelectionProducers","loose50nsRun2"),
                medium = cms.InputTag("eleSelectionProducers","medium"),
                medium25nsRun2 = cms.InputTag("eleSelectionProducers","medium25nsRun2"),
                medium50nsRun2 = cms.InputTag("eleSelectionProducers","medium50nsRun2"),
                tight = cms.InputTag("eleSelectionProducers","tight"),
                tight25nsRun2 = cms.InputTag("eleSelectionProducers","tight25nsRun2"),
                tight50nsRun2 = cms.InputTag("eleSelectionProducers","tight50nsRun2")
            ),
            modifierName = cms.string('EGExtraInfoModifierFromFloatValueMaps'),
            photon_config = cms.PSet(

            )
        ), 
            cms.PSet(
                electron_config = cms.PSet(
                    WP70PU = cms.InputTag("eleSelectionProducers","WP70PU"),
                    WP80PU = cms.InputTag("eleSelectionProducers","WP80PU"),
                    WP90PU = cms.InputTag("eleSelectionProducers","WP90PU"),
                    electronSrc = cms.InputTag("slimmedElectrons"),
                    energySCEleMust = cms.InputTag("eleNewEnergiesProducer","energySCEleMust"),
                    energySCEleMustVar = cms.InputTag("eleNewEnergiesProducer","energySCEleMustVar"),
                    energySCElePho = cms.InputTag("eleNewEnergiesProducer","energySCElePho"),
                    energySCElePhoVar = cms.InputTag("eleNewEnergiesProducer","energySCElePhoVar"),
                    fiducial = cms.InputTag("eleSelectionProducers","fiducial"),
                    loose = cms.InputTag("eleSelectionProducers","loose"),
                    loose25nsRun2 = cms.InputTag("eleSelectionProducers","loose25nsRun2"),
                    loose50nsRun2 = cms.InputTag("eleSelectionProducers","loose50nsRun2"),
                    medium = cms.InputTag("eleSelectionProducers","medium"),
                    medium25nsRun2 = cms.InputTag("eleSelectionProducers","medium25nsRun2"),
                    medium50nsRun2 = cms.InputTag("eleSelectionProducers","medium50nsRun2"),
                    tight = cms.InputTag("eleSelectionProducers","tight"),
                    tight25nsRun2 = cms.InputTag("eleSelectionProducers","tight25nsRun2"),
                    tight50nsRun2 = cms.InputTag("eleSelectionProducers","tight50nsRun2")
                ),
                modifierName = cms.string('EleIDModifierFromValueMaps'),
                photon_config = cms.PSet(

                )
            ))
    ),
    modifyElectrons = cms.bool(True),
    packedPFCandidates = cms.InputTag("packedPFCandidates"),
    recoToPFMap = cms.InputTag("reducedEgamma","reducedGsfElectronPfCandMap"),
    reducedBarrelRecHitCollection = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    reducedEndcapRecHitCollection = cms.InputTag("reducedEgamma","reducedEERecHits"),
    saveNonZSClusterShapes = cms.string('pt > 5'),
    src = cms.InputTag("slimmedElectrons")
)


process.slimmedElectrons = cms.EDProducer("ModifiedElectronProducer",
    modifierConfig = cms.PSet(
        modifications = cms.VPSet()
    ),
    src = cms.InputTag("slimmedElectrons","","@skipCurrentProcess")
)


process.slimmedJets = cms.EDProducer("ModifiedJetProducer",
    modifierConfig = cms.PSet(
        modifications = cms.VPSet()
    ),
    src = cms.InputTag("slimmedJets","","@skipCurrentProcess")
)


process.slimmedJetsAK8 = cms.EDProducer("ModifiedJetProducer",
    modifierConfig = cms.PSet(
        modifications = cms.VPSet()
    ),
    src = cms.InputTag("slimmedJetsAK8","","@skipCurrentProcess")
)


process.slimmedJetsPuppi = cms.EDProducer("ModifiedJetProducer",
    modifierConfig = cms.PSet(
        modifications = cms.VPSet()
    ),
    src = cms.InputTag("slimmedJetsPuppi","","@skipCurrentProcess")
)


process.slimmedMuons = cms.EDProducer("ModifiedMuonProducer",
    modifierConfig = cms.PSet(
        modifications = cms.VPSet()
    ),
    src = cms.InputTag("slimmedMuons","","@skipCurrentProcess")
)


process.slimmedPhotons = cms.EDProducer("ModifiedPhotonProducer",
    modifierConfig = cms.PSet(
        modifications = cms.VPSet()
    ),
    src = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
)


process.slimmedTaus = cms.EDProducer("ModifiedTauProducer",
    modifierConfig = cms.PSet(
        modifications = cms.VPSet()
    ),
    src = cms.InputTag("slimmedTaus","","@skipCurrentProcess")
)


process.tcdsDigis = cms.EDProducer("TcdsRawToDigi",
    InputLabel = cms.InputTag("rawDataCollector")
)


process.tcdsRawToDigi = cms.EDProducer("TcdsRawToDigi",
    InputLabel = cms.InputTag("rawDataCollector")
)


process.totemRPRawToDigi = cms.EDProducer("TotemVFATRawToDigi",
    RawToDigi = cms.PSet(
        BC_fraction = cms.untracked.double(0.6),
        BC_min = cms.untracked.uint32(10),
        EC_fraction = cms.untracked.double(0.6),
        EC_min = cms.untracked.uint32(10),
        printErrorSummary = cms.untracked.uint32(1),
        printUnknownFrameSummary = cms.untracked.uint32(0),
        testBCMostFrequent = cms.uint32(2),
        testCRC = cms.uint32(2),
        testECMostFrequent = cms.uint32(2),
        testFootprint = cms.uint32(2),
        testID = cms.uint32(2),
        verbosity = cms.untracked.uint32(0)
    ),
    RawUnpacking = cms.PSet(

    ),
    fedIds = cms.vuint32(),
    rawDataTag = cms.InputTag("rawDataCollector"),
    subSystem = cms.string('RP')
)


process.totemTriggerRawToDigi = cms.EDProducer("TotemTriggerRawToDigi",
    fedId = cms.uint32(0),
    rawDataTag = cms.InputTag("rawDataCollector")
)


process.totemVFATRawToDigi = cms.EDProducer("TotemVFATRawToDigi",
    RawToDigi = cms.PSet(
        BC_fraction = cms.untracked.double(0.6),
        BC_min = cms.untracked.uint32(10),
        EC_fraction = cms.untracked.double(0.6),
        EC_min = cms.untracked.uint32(10),
        printErrorSummary = cms.untracked.uint32(1),
        printUnknownFrameSummary = cms.untracked.uint32(0),
        testBCMostFrequent = cms.uint32(2),
        testCRC = cms.uint32(2),
        testECMostFrequent = cms.uint32(2),
        testFootprint = cms.uint32(2),
        testID = cms.uint32(2),
        verbosity = cms.untracked.uint32(0)
    ),
    RawUnpacking = cms.PSet(

    ),
    fedIds = cms.vuint32(),
    rawDataTag = cms.InputTag(""),
    subSystem = cms.string('')
)


process.uncleanedHybridSuperClusters = cms.EDProducer("HybridClusterProducer",
    HybridBarrelSeedThr = cms.double(1.0),
    RecHitFlagToBeExcluded = cms.vstring('kFaultyHardware', 
        'kTowerRecovered', 
        'kDead'),
    RecHitSeverityToBeExcluded = cms.vstring(),
    basicclusterCollection = cms.string('hybridBarrelBasicClusters'),
    clustershapecollection = cms.string(''),
    dynamicEThresh = cms.bool(False),
    dynamicPhiRoad = cms.bool(False),
    eThreshA = cms.double(0.003),
    eThreshB = cms.double(0.1),
    eseed = cms.double(0.35),
    ethresh = cms.double(0.1),
    ewing = cms.double(0.0),
    excludeFlagged = cms.bool(False),
    posCalcParameters = cms.PSet(
        LogWeighted = cms.bool(True),
        T0_barl = cms.double(7.4),
        T0_endc = cms.double(3.1),
        T0_endcPresh = cms.double(1.2),
        W0 = cms.double(4.2),
        X0 = cms.double(0.89)
    ),
    recHitsCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    shapeAssociation = cms.string('hybridShapeAssoc'),
    step = cms.int32(17),
    superclusterCollection = cms.string(''),
    useEtForXi = cms.bool(True),
    xi = cms.double(0.0)
)


process.uncleanedOnlyCorrectedHybridSuperClusters = cms.EDProducer("EgammaSCCorrectionMaker",
    applyCrackCorrection = cms.bool(True),
    applyEnergyCorrection = cms.bool(True),
    applyLocalContCorrection = cms.bool(True),
    corectedSuperClusterCollection = cms.string(''),
    crackCorrectorName = cms.string('EcalClusterCrackCorrection'),
    energyCorrectorName = cms.string('EcalClusterEnergyCorrectionObjectSpecific'),
    etThresh = cms.double(0.0),
    hyb_fCorrPset = cms.PSet(
        brLinearHighThr = cms.double(8.0),
        brLinearLowThr = cms.double(1.1),
        fBremVec = cms.vdouble(-0.04382, 0.1169, 0.9267, -0.0009413, 1.419),
        fEtEtaVec = cms.vdouble(0, 1.00121, -0.63672, 0, 0, 
            0, 0.5655, 6.457, 0.5081, 8.0, 
            1.023, -0.00181)
    ),
    localContCorrectorName = cms.string('EcalBasicClusterLocalContCorrection'),
    modeEB = cms.int32(0),
    modeEE = cms.int32(0),
    rawSuperClusterProducer = cms.InputTag("hybridSuperClusters","uncleanOnlyHybridSuperClusters"),
    recHitProducer = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    sigmaElectronicNoise = cms.double(0.03),
    superClusterAlgo = cms.string('Hybrid')
)


process.uncleanedOnlyCorrectedMulti5x5SuperClustersWithPreshower = cms.EDProducer("EgammaSCCorrectionMaker",
    VerbosityLevel = cms.string('ERROR'),
    applyCrackCorrection = cms.bool(True),
    applyEnergyCorrection = cms.bool(True),
    applyLocalContCorrection = cms.bool(False),
    corectedSuperClusterCollection = cms.string(''),
    crackCorrectorName = cms.string('EcalClusterCrackCorrection'),
    energyCorrectorName = cms.string('EcalClusterEnergyCorrectionObjectSpecific'),
    etThresh = cms.double(0.0),
    fix_fCorrPset = cms.PSet(
        brLinearHighThr = cms.double(6.0),
        brLinearLowThr = cms.double(0.9),
        fBremVec = cms.vdouble(-0.05228, 0.08738, 0.9508, 0.002677, 1.221),
        fEtEtaVec = cms.vdouble(1, -0.4386, -32.38, 0.6372, 15.67, 
            -0.0928, -2.462, 1.138, 20.93)
    ),
    localContCorrectorName = cms.string('EcalBasicClusterLocalContCorrection'),
    modeEB = cms.int32(0),
    modeEE = cms.int32(0),
    rawSuperClusterProducer = cms.InputTag("uncleanedOnlyMulti5x5SuperClustersWithPreshower"),
    recHitProducer = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    sigmaElectronicNoise = cms.double(0.15),
    superClusterAlgo = cms.string('Multi5x5')
)


process.uncleanedOnlyMulti5x5SuperClustersWithPreshower = cms.EDProducer("PreshowerPhiClusterProducer",
    assocSClusterCollection = cms.string(''),
    endcapSClusterProducer = cms.InputTag("multi5x5SuperClusters","uncleanOnlyMulti5x5EndcapSuperClusters"),
    esPhiClusterDeltaEta = cms.double(0.15),
    esPhiClusterDeltaPhi = cms.double(0.12),
    esStripEnergyCut = cms.double(0.0),
    etThresh = cms.double(0.0),
    preshClusterCollectionX = cms.string('preshowerXClusters'),
    preshClusterCollectionY = cms.string('preshowerYClusters'),
    preshRecHitProducer = cms.InputTag("ecalPreshowerRecHit","EcalRecHitsES")
)


process.zdcreco = cms.EDProducer("ZdcHitReconstructor",
    AuxTSvec = cms.vint32(4, 5, 6, 7),
    Subdetector = cms.string('ZDC'),
    correctForPhaseContainment = cms.bool(False),
    correctForTimeslew = cms.bool(False),
    correctTiming = cms.bool(True),
    correctionPhaseNS = cms.double(0.0),
    digiLabel = cms.InputTag("hcalDigis"),
    dropZSmarkedPassed = cms.bool(True),
    lowGainFrac = cms.double(8.15),
    lowGainOffset = cms.int32(1),
    recoMethod = cms.int32(2),
    saturationParameters = cms.PSet(
        maxADCvalue = cms.int32(127)
    ),
    setHSCPFlags = cms.bool(True),
    setNoiseFlags = cms.bool(True),
    setSaturationFlags = cms.bool(True),
    setTimingTrustFlags = cms.bool(False)
)


process.MinEleNumberFilter = cms.EDFilter("CandViewCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("slimmedElectrons")
)


process.MinMuonNumberFilter = cms.EDFilter("CandViewCountFilter",
    minNumber = cms.uint32(2),
    src = cms.InputTag("muons")
)


process.MinPhoNumberFilter = cms.EDFilter("CandViewCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("gedPhotons")
)


process.MuFilter = cms.EDFilter("CandViewCountFilter",
    minNumber = cms.uint32(2),
    src = cms.InputTag("PassingMuonVeryLooseId")
)


process.NtupleFilter = cms.EDFilter("HLTHighLevel",
    HLTPaths = cms.vstring('pathALCARECOEcalUncalZElectron', 
        'pathALCARECOEcalUncalWElectron', 
        'pathALCARECOEcalCalZElectron', 
        'pathALCARECOEcalCalWElectron', 
        'pathALCARECOEcalUncalZSCElectron', 
        'pathALCARECOEcalCalZSCElectron', 
        'pathALCARECOEcalUncalSingleElectron', 
        'pathALCARECOEcalCalSingleElectron'),
    TriggerResultsTag = cms.InputTag("TriggerResults","","RECO"),
    andOr = cms.bool(True),
    eventSetupPathsKey = cms.string(''),
    throw = cms.bool(False)
)


process.PassingMuonVeryLooseId = cms.EDFilter("MuonRefSelector",
    cut = cms.string('(isPFMuon) && (isGlobalMuon || isTrackerMuon)'),
    src = cms.InputTag("muons")
)


process.PassingPhotonVeryLooseId = cms.EDFilter("PhotonRefSelector",
    cut = cms.string('(abs(superCluster.eta)<3) && (pt > 10)&& ( (eta<1.479 && sigmaIetaIeta<0.02 && hadronicOverEm<0.06 )||( eta>=1.479 && sigmaIetaIeta<0.04 && hadronicOverEm<0.06 ) )'),
    src = cms.InputTag("gedPhotons")
)


process.PassingVetoId = cms.EDFilter("GsfElectronRefSelector",
    cut = cms.string("(abs(superCluster.eta)<3) && (energy*sin(superClusterPosition.theta)> 15) && (gsfTrack.hitPattern().numberOfHits(\'MISSING_INNER_HITS\')<=2) && ((isEB && ( ((pfIsolationVariables().sumChargedHadronPt + max(0.0,pfIsolationVariables().sumNeutralHadronEt + pfIsolationVariables().sumPhotonEt - 0.5 * pfIsolationVariables().sumPUPt))/p4.pt)<0.164369) && (full5x5_sigmaIetaIeta<0.011100) && ( - \t0.252044<deltaPhiSuperClusterTrackAtVtx< \t0.252044 ) && ( -0.016315<deltaEtaSuperClusterTrackAtVtx<0.016315 ) && (hadronicOverEm<0.345843)) || (isEE && (gsfTrack.hitPattern().numberOfHits(\'MISSING_INNER_HITS\')<=3) && ( ((pfIsolationVariables().sumChargedHadronPt + max(0.0,pfIsolationVariables().sumNeutralHadronEt + pfIsolationVariables().sumPhotonEt - 0.5 * pfIsolationVariables().sumPUPt))/p4.pt)<0.212604 ) && (full5x5_sigmaIetaIeta<0.033987) && ( -0.245263<deltaPhiSuperClusterTrackAtVtx<0.245263 ) && ( -0.010671<deltaEtaSuperClusterTrackAtVtx<0.010671 ) && (hadronicOverEm<0.134691) ))"),
    src = cms.InputTag("slimmedElectrons")
)


process.PhoFilter = cms.EDFilter("CandViewCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("PassingPhotonVeryLooseId")
)


process.SCselector = cms.EDFilter("SuperClusterSelector",
    cut = cms.string('(eta>2.4 || eta<-2.4) && (energy*sin(position.theta)> 15)'),
    src = cms.InputTag("correctedMulti5x5SuperClustersWithPreshower")
)


process.WFilterMC = cms.EDFilter("CandViewCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("combW")
)


process.WZFilter = cms.EDFilter("CandViewCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("WZSelector")
)


process.WenuFilter = cms.EDFilter("CandViewCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("WenuSelector")
)


process.ZFilterMC = cms.EDFilter("CandViewCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("combZ")
)


process.ZSCFilter = cms.EDFilter("CandViewCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("EleSCSelector")
)


process.ZSCHltFilter = cms.EDFilter("HLTHighLevel",
    HLTPaths = cms.vstring('HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele15_CaloIdT_CaloIsoVL_trackless_v*'),
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    andOr = cms.bool(True),
    eventSetupPathsKey = cms.string(''),
    throw = cms.bool(False)
)


process.ZeeFilter = cms.EDFilter("CandViewCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("ZeeSelector")
)


process.ZmmgDimuonFilter = cms.EDFilter("CandViewCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("ZmmgDimuons")
)


process.ZmmgFilter = cms.EDFilter("CandViewCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("ZmmgCandidates")
)


process.ZmmgHLTFilter = cms.EDFilter("HLTHighLevel",
    HLTPaths = cms.vstring('HLT_Mu*', 
        'HLT_IsoMu*', 
        'HLT_DoubleMu*'),
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    andOr = cms.bool(True),
    eventSetupPathsKey = cms.string(''),
    throw = cms.bool(False)
)


process.ZmmgLeadingMuons = cms.EDFilter("MuonSelector",
    cut = cms.string('pt > 20'),
    filter = cms.bool(True),
    src = cms.InputTag("ZmmgTrailingMuons")
)


process.ZmmgPhotons = cms.EDFilter("CandViewSelector",
    cut = cms.string('et > 5'),
    filter = cms.bool(True),
    src = cms.InputTag("ZmmgPhotonCandidates")
)


process.ZmmgTrailingMuons = cms.EDFilter("MuonSelector",
    cut = cms.string('pt > 10 && \n                        abs(eta) < 2.4 && \n                        isGlobalMuon = 1 && \n                        isTrackerMuon = 1 && \n                        abs(innerTrack().dxy)<2.0'),
    filter = cms.bool(True),
    src = cms.InputTag("muons")
)


process.genEleFromW = cms.EDFilter("CandViewSelector",
    cut = cms.string('(pdgId == 11 || pdgId == -11) && eta <2.5 && eta>-2.5 && pt > 25 && (mother(0).pdgId == 24 || mother(0).pdgId == -24)'),
    src = cms.InputTag("genParticles")
)


process.genEleFromZ = cms.EDFilter("CandViewSelector",
    cut = cms.string('(pdgId == 11 || pdgId == -11) && eta <2.5 && eta>-2.5 && pt > 15 && mother(0).pdgId == 23'),
    src = cms.InputTag("genParticles")
)


process.genNuFromW = cms.EDFilter("CandViewSelector",
    cut = cms.string('(pdgId == 12 || pdgId == -12) && (mother(0).pdgId == 24 || mother(0).pdgId == -24)'),
    src = cms.InputTag("genParticles")
)


process.hltHighLevel = cms.EDFilter("HLTHighLevel",
    HLTPaths = cms.vstring(),
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    andOr = cms.bool(True),
    eventSetupPathsKey = cms.string(''),
    throw = cms.bool(True)
)


process.jsonFilter = cms.EDFilter("JsonFilter",
    jsonFileName = cms.string('/afs/cern.ch/work/y/yhaddad/80X_ECALELF_ntuples/JSON_2016/RUN2016G-281613-282037_13TeV_PromptReco_JSON_NoL1T.txt')
)


process.selectedECALElectrons = cms.EDFilter("GsfElectronRefSelector",
    cut = cms.string('(abs(superCluster.eta)<3) && (energy*sin(superClusterPosition.theta)> 15)'),
    src = cms.InputTag("slimmedElectrons")
)


process.selectedECALMuons = cms.EDFilter("MuonRefSelector",
    cut = cms.string(''),
    src = cms.InputTag("muons")
)


process.selectedECALPhotons = cms.EDFilter("PhotonRefSelector",
    cut = cms.string('(abs(superCluster.eta)<3) && (pt > 10)'),
    src = cms.InputTag("gedPhotons")
)


process.PUDumper = cms.EDAnalyzer("PUDumper",
    pileupSummary = cms.InputTag("addPileupInfo")
)


process.zNtupleDumper = cms.EDAnalyzer("ZNtupleDumper",
    BeamSpotCollection = cms.InputTag("offlineBeamSpot"),
    EESuperClusterCollection = cms.InputTag("reducedEgamma","reducedSuperClusters"),
    SelectEvents = cms.vstring('NtuplePath'),
    WZSkimResultsCollection = cms.InputTag("TriggerResults"),
    conversionCollection = cms.InputTag("allConversions"),
    doEleIDTree = cms.bool(False),
    doExtraCalibTree = cms.bool(False),
    doHighEta_LowerEtaCut = cms.double(2.4),
    doStandardTree = cms.bool(True),
    eleID_loose = cms.string('cutBasedElectronID-Spring15-25ns-V1-standalone-loose'),
    eleID_medium = cms.string('cutBasedElectronID-Spring15-25ns-V1-standalone-medium'),
    eleID_tight = cms.string('cutBasedElectronID-Spring15-25ns-V1-standalone-tight'),
    electronCollection = cms.InputTag("slimmedECALELFElectrons"),
    foutName = cms.string('ntuple.root'),
    fsrWeightCollection = cms.InputTag("fsrWeight"),
    hltPaths = cms.vstring(),
    isPartGun = cms.bool(False),
    jsonFileName = cms.string(''),
    metCollection = cms.InputTag("pfMet"),
    muonCollection = cms.InputTag("patMuons"),
    pdfWeightCollections = cms.VInputTag(),
    photonCollection = cms.InputTag("patPhotons"),
    pileupInfo = cms.InputTag("slimmedAddPileupInfo"),
    recHitCollectionEB = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    recHitCollectionEE = cms.InputTag("reducedEgamma","reducedEERecHits"),
    recHitCollectionES = cms.InputTag("reducedEgamma","reducedESRecHits"),
    rhoFastJet = cms.InputTag("fixedGridRhoFastjetAll"),
    triggerResultsCollection = cms.InputTag("TriggerResults","","HLT"),
    uncalibRecHitCollectionEB = cms.InputTag("ecalMultiFitUncalibRecHit","EcalUncalibRecHitsEB"),
    uncalibRecHitCollectionEE = cms.InputTag("ecalMultiFitUncalibRecHit","EcalUncalibRecHitsEE"),
    useIDforPresel = cms.bool(False),
    vertexCollection = cms.InputTag("offlineSlimmedPrimaryVertices"),
    weakWeightCollection = cms.InputTag("weakWeight")
)


process.outputALCARAW = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalUncalSingleElectron')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('alcaraw.root'),
    maxSize = cms.untracked.int32(5120000),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *EcalRecHit*_*ecalPreshowerRecHit*_*EcalRecHitsES*_*', 
        'keep *_ecalDigis_*_*', 
        'keep *EcalTriggerPrimitiveDigi*_ecalDigis_*_*', 
        'keep *_ecalPreshowerDigis_*_*', 
        'keep *_ecalDetIdToBeRecovered_*_*', 
        'keep reco*Clusters_pfElectronTranslator_*_*', 
        'drop recoCaloClusters_*_*_*', 
        'drop recoSuperClusters_*_*_*', 
        'drop recoPreshowerCluster*_*_*_*', 
        'drop *EcalRecHit*_reducedEcalRecHitsES*_*_*', 
        'drop *EcalRecHit*_*_*_*', 
        'keep reco*Clusters_pfElectronTranslator_*_*')
)


process.outputALCARECO = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalCalSingleElectron')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('alcareco.root'),
    maxSize = cms.untracked.int32(5120000),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *EcalRecHit*_*ecalPreshowerRecHit*_*EcalRecHitsES*_*', 
        'drop reco*Clusters_hfEMClusters_*_*', 
        'drop reco*Clusters_pfPhotonTranslator_*_*', 
        'drop *EcalRecHit*_ecalRecHit_*_*', 
        'drop *_*Cleaned_*_*', 
        'drop *_*cleaned*_*_*', 
        'drop *_*Unclean*_*_*', 
        'drop *_*unclean*_*_*', 
        'drop *_*_*Unclean*_*', 
        'drop *_*_*unclean*_*', 
        'keep recoSuperClusters_*_uncleanOnly_*', 
        'drop *_*_multi5x5Barrel*Clusters_*', 
        'drop *_dqmL1ExtraParticles_*_*', 
        'drop recoSuperClusters_mergedSuperClusters_*_*', 
        'keep *CaloCluster*_*alCaIsolatedElectrons*_*alcaCaloCluster*_*')
)


process.outputALCARERECO = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARERECOEcalCalElectron')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('EcalRecalElectron.root'),
    maxSize = cms.untracked.int32(5120000),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *EcalRecHit*_*ecalPreshowerRecHit*_*EcalRecHitsES*_*', 
        'drop reco*Clusters_hfEMClusters_*_*', 
        'drop reco*Clusters_pfPhotonTranslator_*_*', 
        'drop *EcalRecHit*_ecalRecHit_*_*', 
        'drop *_*Cleaned_*_*', 
        'drop *_*cleaned*_*_*', 
        'drop *_*Unclean*_*_*', 
        'drop *_*unclean*_*_*', 
        'drop *_*_*Unclean*_*', 
        'drop *_*_*unclean*_*', 
        'keep recoSuperClusters_*_uncleanOnly_*', 
        'drop *_*_multi5x5Barrel*Clusters_*', 
        'drop *_dqmL1ExtraParticles_*_*', 
        'drop recoSuperClusters_mergedSuperClusters_*_*', 
        'keep *CaloCluster*_*alCaIsolatedElectrons*_*alcaCaloCluster*_*')
)


process.outputRECO = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('RECO.root'),
    maxSize = cms.untracked.int32(5120000),
    outputCommands = cms.untracked.vstring('keep *')
)


process.postPatSequence = cms.Sequence(process.eleSelectionProducers+process.eleNewEnergiesProducer+process.slimmedECALELFElectrons)


process.ZmmgDimuonSequence = cms.Sequence(process.ZmmgTrailingMuons+process.ZmmgLeadingMuons+process.ZmmgDimuons+process.ZmmgDimuonFilter)


process.NtupleFilterSeq = cms.Sequence()


process.hcalLocalRecoSequence = cms.Sequence(process.hbheprereco+process.hfreco+process.horeco+process.zdcreco)


process.preFilterSeq = cms.Sequence(process.MinEleNumberFilter)


process.filterSeq = cms.Sequence()


process.hcalLocalRecoSequenceNZS = cms.Sequence(process.hbherecoMB+process.hfrecoMB+process.horecoMB)


process.ALCARECOEcalCalElectronNonECALSeq = cms.Sequence(process.kt6PFJetsForRhoCorrection+process.alcaElectronTracksReducer)


process.pfClusteringPS = cms.Sequence(process.particleFlowRecHitPS+process.particleFlowClusterPS)


process.PUDumperSeq = cms.Sequence()


process.alcarecoElectronTracksReducerSeq = cms.Sequence(process.alcaElectronTracksReducer)


process.checkMCWSeq = cms.Sequence(process.genEleFromW+process.genNuFromW+process.combW+process.WFilterMC)


process.ZmmgPhotonSequence = cms.Sequence(process.ZmmgMergedSuperClusters+process.ZmmgPhotonCandidates+process.ZmmgPhotons)


process.ecalUncalibRecHitSequence = cms.Sequence(process.ecalMultiFitUncalibRecHit+process.ecalDetIdToBeRecovered)


process.pfClusteringECAL = cms.Sequence(process.particleFlowRecHitECAL+process.particleFlowClusterECALUncorrected+process.particleFlowClusterECAL)


process.modifyPrimaryPhysicsObjects = cms.Sequence(process.electronMVAValueMapProducer+process.photonIDValueMapProducer+process.photonMVAValueMapProducer+process.slimmedElectrons+process.slimmedPhotons+process.slimmedMuons+process.slimmedTaus+process.slimmedJets+process.slimmedJetsAK8+process.slimmedJetsPuppi)


process.uncalibRecHitSeq = cms.Sequence(process.ecalDigis+process.ecalPreshowerDigis)


process.prePatSequence = cms.Sequence()


process.ecalRecHitSequence = cms.Sequence(process.ecalRecHit+process.ecalCompactTrigPrim+process.ecalTPSkim+process.ecalPreshowerRecHit)


process.checkMCZSeq = cms.Sequence(process.genEleFromZ+process.combZ+process.ZFilterMC)


process.eleIsoSequence = cms.Sequence(process.elPFIsoDepositChargedGsf+process.elPFIsoDepositChargedAllGsf+process.elPFIsoDepositNeutralGsf+process.elPFIsoDepositGammaGsf+process.elPFIsoDepositPUGsf+(process.elPFIsoValueCharged03PFIdGsf+process.elPFIsoValueChargedAll03PFIdGsf+process.elPFIsoValueGamma03PFIdGsf+process.elPFIsoValueNeutral03PFIdGsf+process.elPFIsoValuePU03PFIdGsf))


process.ecalUncalibRecHitSequence53X = cms.Sequence(process.ecalGlobalUncalibRecHit+process.ecalDetIdToBeRecovered)


process.seqALCARECOEcalCalPhoton = cms.Sequence(process.alCaIsolatedElectrons+process.kt6PFJetsForRhoCorrection)


process.muSelSeq = cms.Sequence(process.selectedECALMuons+process.selectedECALPhotons+process.PassingMuonVeryLooseId+process.PassingPhotonVeryLooseId+process.MuFilter+process.PhoFilter+process.SCselector+process.eleSC)


process.rerecoPFClusteringSeq = cms.Sequence(process.pfClusteringPS+process.pfClusteringECAL)


process.pfIsoEgamma = cms.Sequence()


process.pfClusteringHBHEHF = cms.Sequence(process.particleFlowRecHitHBHE+process.particleFlowRecHitHF+process.particleFlowClusterHBHE+process.particleFlowClusterHF+process.particleFlowClusterHCAL)


process.rhoFastJetSeq = cms.Sequence()


process.multi5x5ClusteringSequence = cms.Sequence(process.multi5x5BasicClustersCleaned+process.multi5x5SuperClustersCleaned+process.multi5x5BasicClustersUncleaned+process.multi5x5SuperClustersUncleaned+process.multi5x5SuperClusters+process.multi5x5SuperClustersWithPreshower)


process.multi5x5PreshowerClusteringSequence = cms.Sequence(process.correctedMulti5x5SuperClustersWithPreshower+process.multi5x5PreshowerClusterShape+process.uncleanedOnlyMulti5x5SuperClustersWithPreshower+process.uncleanedOnlyCorrectedMulti5x5SuperClustersWithPreshower)


process.ALCARECOEcalUncalElectronECALSeq = cms.Sequence(process.uncalibRecHitSeq)


process.EIsequence = cms.Sequence(process.modifyPrimaryPhysicsObjects)


process.eleSelSeq = cms.Sequence(process.selectedECALElectrons+process.PassingVetoId+process.SCselector+process.eleSC)


process.hcalGlobalRecoSequence = cms.Sequence(process.hbhereco)


process.ecalLocalRecoSequence = cms.Sequence(process.ecalUncalibRecHitSequence+process.ecalRecHitSequence)


process.trivialCond = cms.Sequence()


process.reducedHcalRecHitsSequence = cms.Sequence(process.reducedHcalRecHits)


process.seldigis = cms.Sequence(process.selectDigi)


process.alcarecoEcalRecHitReducerSeq = cms.Sequence(process.alCaIsolatedElectrons)


process.ZmmgSequence = cms.Sequence(process.ZmmgCandidates+process.ZmmgFilter)


process.hybridClusteringSequence = cms.Sequence(process.cleanedHybridSuperClusters+process.uncleanedHybridSuperClusters+process.hybridSuperClusters+process.correctedHybridSuperClusters+process.uncleanedOnlyCorrectedHybridSuperClusters)


process.patTriggerMatchSeq = cms.Sequence(process.patTrigger+process.PatElectronTriggerMatchHLTEle_Ele20SC4Mass50v7+process.PatElectronsTriggerMatch+process.patTriggerEvent)


process.pfClusteringHO = cms.Sequence(process.particleFlowRecHitHO+process.particleFlowClusterHO)


process.L1TRawToDigi_Legacy = cms.Sequence(process.csctfDigis+process.dttfDigis+process.gctDigis+process.gtDigis+process.gtEvmDigis)


process.ALCARECOEcalCalElectronECALSeq = cms.Sequence(process.alCaIsolatedElectrons)


process.particleFlowSuperClusteringSequence = cms.Sequence(process.particleFlowSuperClusterECAL)


process.particleFlowClusterWithoutHO = cms.Sequence(process.pfClusteringPS+process.pfClusteringECAL+process.pfClusteringHBHEHF)


process.L1TRawToDigi = cms.Sequence(process.L1TRawToDigi_Legacy)


process.calolocalreco = cms.Sequence(process.ecalLocalRecoSequence+process.hcalLocalRecoSequence)


process.reducedEcalRecHitsSequenceEcalOnly = cms.Sequence(process.interestingEcalDetIdEB+process.interestingEcalDetIdEBU+process.interestingEcalDetIdEE+process.reducedEcalRecHitsEB+process.reducedEcalRecHitsEE+process.seldigis)


process.ALCARECOEcalCalElectronSeq = cms.Sequence(process.ALCARECOEcalCalElectronNonECALSeq+process.ALCARECOEcalCalElectronECALSeq)


process.seqALCARECOEcalUncalElectron = cms.Sequence(process.ALCARECOEcalCalElectronNonECALSeq+process.ALCARECOEcalUncalElectronECALSeq)


process.particleFlowCluster = cms.Sequence(process.pfClusteringPS+process.pfClusteringECAL+process.pfClusteringHBHEHF+process.pfClusteringHO)


process.ecalClustersNoPFBox = cms.Sequence(process.hybridClusteringSequence+process.multi5x5ClusteringSequence+process.multi5x5PreshowerClusteringSequence)


process.RawToDigi = cms.Sequence(process.L1TRawToDigi+process.siPixelDigis+process.siStripDigis+process.ecalDigis+process.ecalPreshowerDigis+process.hcalDigis+process.muonCSCDigis+process.muonDTDigis+process.muonRPCDigis+process.castorDigis+process.scalersRawToDigi+process.tcdsDigis)


process.pfisoALCARECO = cms.Sequence(process.eleIsoSequence)


process.patSequenceMC = cms.Sequence(process.electronMatch+process.prePatSequence+process.patElectrons+process.postPatSequence)


process.ZmmgSkimSeq = cms.Sequence(process.ZmmgHLTFilter+process.ZmmgDimuonSequence+process.ZmmgPhotonSequence+process.ZmmgSequence)


process.patSequence = cms.Sequence(process.prePatSequence+process.postPatSequence)


process.reducedEcalRecHitsSequence = cms.Sequence(process.interestingEcalDetIdEB+process.interestingEcalDetIdEBU+process.interestingEcalDetIdEE+process.interestingEcalDetIdPFEB+process.interestingEcalDetIdPFEE+process.interestingEcalDetIdPFES+process.interestingEcalDetIdRefinedEB+process.interestingEcalDetIdRefinedEE+process.interestingEcalDetIdRefinedES+process.interestingTrackEcalDetIds+process.reducedEcalRecHitsEB+process.reducedEcalRecHitsEE+process.seldigis+process.reducedEcalRecHitsES)


process.RawToDigi_noTk = cms.Sequence(process.L1TRawToDigi+process.ecalDigis+process.ecalPreshowerDigis+process.hcalDigis+process.muonCSCDigis+process.muonDTDigis+process.muonRPCDigis+process.castorDigis+process.scalersRawToDigi+process.tcdsDigis)


process.caloglobalreco = cms.Sequence(process.hcalGlobalRecoSequence)


process.FilterMuSeq = cms.Sequence(process.muSelSeq+process.ZeeSelector+process.WenuSelector+process.EleSCSelector+process.WZSelector)


process.selectorProducerSeq = cms.Sequence(process.eleSelSeq+process.ZeeSelector+process.WenuSelector+process.EleSCSelector+process.WZSelector)


process.recoECALSeq = cms.Sequence(process.ecalLocalRecoSequence)


process.calolocalrecoNZS = cms.Sequence(process.ecalLocalRecoSequence+process.hcalLocalRecoSequence+process.hcalLocalRecoSequenceNZS)


process.ntupleSeq = cms.Sequence(process.jsonFilter+process.EIsequence+process.patSequence)


process.ecalClusters = cms.Sequence(process.ecalClustersNoPFBox+process.particleFlowSuperClusteringSequence)


process.ZSCSkimFilterSeq = cms.Sequence(process.preFilterSeq+process.selectorProducerSeq+~process.ZeeFilter+process.ZSCFilter)


process.WenuSkimFilterSeq = cms.Sequence(process.preFilterSeq+process.selectorProducerSeq+~process.ZeeFilter+~process.ZSCFilter+process.WenuFilter)


process.seqALCARECOEcalUncalZSCElectron = cms.Sequence(process.ZSCSkimFilterSeq+process.ALCARECOEcalCalElectronNonECALSeq+process.ALCARECOEcalUncalElectronECALSeq)


process.ZeeSkimFilterSeq = cms.Sequence(process.preFilterSeq+process.selectorProducerSeq+process.ZeeFilter)


process.ecalClusteringSeq = cms.Sequence(process.ecalClusters+process.electronRecalibSCAssociator)


process.seqALCARECOEcalCalZSCElectron = cms.Sequence(process.ZSCSkimFilterSeq+process.ALCARECOEcalCalElectronSeq)


process.seqALCARECOEcalUncalWElectron = cms.Sequence(process.WenuSkimFilterSeq+process.ALCARECOEcalCalElectronNonECALSeq+process.ALCARECOEcalUncalElectronECALSeq)


process.seqALCARECOEcalCalZElectron = cms.Sequence(process.ZeeSkimFilterSeq+process.ALCARECOEcalCalElectronSeq)


process.seqALCARECOEcalUncalZElectron = cms.Sequence(process.ZeeSkimFilterSeq+process.ALCARECOEcalCalElectronNonECALSeq+process.ALCARECOEcalUncalElectronECALSeq)


process.seqALCARECOEcalCalWElectron = cms.Sequence(process.WenuSkimFilterSeq+process.ALCARECOEcalCalElectronSeq)


process.rerecoECALSeq = cms.Sequence(process.recoECALSeq+process.rerecoPFClusteringSeq+process.ecalClusteringSeq)


process.seqALCARECOEcalRecalElectron = cms.Sequence(process.bunchSpacingProducer+process.rerecoECALSeq+process.selectorProducerSeq+process.ALCARECOEcalCalElectronECALSeq)


process.alcarerecoSeq = cms.Sequence(process.trivialCond+process.seqALCARECOEcalRecalElectron)


process.pathALCARECOEcalUncalSingleElectron = cms.Path(process.PUDumperSeq+process.filterSeq+process.seqALCARECOEcalUncalElectron)


process.pathALCARECOEcalUncalZElectron = cms.Path(process.PUDumperSeq+process.filterSeq+process.preFilterSeq+process.seqALCARECOEcalUncalZElectron)


process.pathALCARECOEcalUncalZSCElectron = cms.Path(process.PUDumperSeq+process.filterSeq+process.preFilterSeq+~process.ZeeFilter+process.ZSCFilter+process.seqALCARECOEcalUncalZSCElectron)


process.pathALCARECOEcalUncalWElectron = cms.Path(process.PUDumperSeq+process.filterSeq+process.preFilterSeq+~process.ZeeFilter+~process.ZSCFilter+process.WenuFilter+process.seqALCARECOEcalUncalWElectron)


process.pathALCARECOEcalUncalZmmgPhoton = cms.Path(process.PUDumperSeq+process.filterSeq+process.FilterMuSeq+process.ZmmgSkimSeq+~process.ZeeFilter+~process.ZSCFilter+~process.WenuFilter+process.seqALCARECOEcalUncalElectron)


process.pathALCARERECOEcalCalElectron = cms.Path(process.alcarerecoSeq+(process.ntupleSeq))


process.pathALCARECOEcalCalSingleElectron = cms.Path(process.PUDumperSeq+process.filterSeq+process.pfIsoEgamma+process.ALCARECOEcalCalElectronSeq)


process.pathALCARECOEcalCalZElectron = cms.Path(process.PUDumperSeq+process.filterSeq+process.ZeeSkimFilterSeq+process.pfIsoEgamma+process.ALCARECOEcalCalElectronSeq)


process.pathALCARECOEcalCalWElectron = cms.Path(process.PUDumperSeq+process.filterSeq+process.WenuSkimFilterSeq+process.pfIsoEgamma+process.ALCARECOEcalCalElectronSeq)


process.pathALCARECOEcalCalZSCElectron = cms.Path(process.PUDumperSeq+process.filterSeq+process.ZSCSkimFilterSeq+process.pfIsoEgamma+process.ALCARECOEcalCalElectronSeq)


process.pathALCARECOEcalCalZmmgPhoton = cms.Path(process.PUDumperSeq+process.filterSeq+process.FilterMuSeq+process.ZmmgSkimSeq+~process.ZeeFilter+~process.ZSCFilter+~process.WenuFilter+process.pfIsoEgamma+process.seqALCARECOEcalCalPhoton)


process.NtuplePath = cms.Path(process.filterSeq+process.preFilterSeq+process.NtupleFilterSeq+process.ntupleSeq)


process.NtupleEndPath = cms.EndPath(process.zNtupleDumper)


process.DQMStore = cms.Service("DQMStore",
    LSbasedMode = cms.untracked.bool(False),
    collateHistograms = cms.untracked.bool(False),
    enableMultiThread = cms.untracked.bool(False),
    forceResetOnBeginLumi = cms.untracked.bool(False),
    referenceFileName = cms.untracked.string(''),
    verbose = cms.untracked.int32(0),
    verboseQT = cms.untracked.int32(0)
)


process.MessageLogger = cms.Service("MessageLogger",
    FrameworkJobReport = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring('FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary'),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1000)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(100)
        ),
        noTimeStamps = cms.untracked.bool(False),
        optionalPSet = cms.untracked.bool(True),
        threshold = cms.untracked.string('INFO')
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    destinations = cms.untracked.vstring('warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport'),
    infos = cms.untracked.PSet(
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        optionalPSet = cms.untracked.bool(True),
        placeholder = cms.untracked.bool(True)
    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    suppressDebug = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring('particleFlowDisplacedVertexCandidate'),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    )
)


process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    LHCTransport = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    MuonSimHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(987346)
    ),
    VtxSmeared = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(98765432)
    ),
    ecalPreshowerRecHit = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(6541321)
    ),
    ecalRecHit = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(654321)
    ),
    externalLHEProducer = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(234567)
    ),
    famosPileUp = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    famosSimHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(13579)
    ),
    g4SimHits = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(11)
    ),
    generator = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hbhereco = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hfreco = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hiSignal = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hiSignalG4SimHits = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(11)
    ),
    hiSignalLHCTransport = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(88776655)
    ),
    horeco = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    l1ParamMuons = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(6453209)
    ),
    mix = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixData = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixGenPU = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixRecoTracks = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixSimCaloHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    paramMuons = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(54525)
    ),
    saveFileName = cms.untracked.string(''),
    siTrackerGaussianSmearingRecHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(24680)
    ),
    simBeamSpotFilter = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    simMuonCSCDigis = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(11223344)
    ),
    simMuonDTDigis = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simMuonRPCDigis = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simSiStripDigiSimLink = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(1234567)
    )
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring('HCAL', 
        'ZDC', 
        'CASTOR', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER')
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    )
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP")


process.CastorDbProducer = cms.ESProducer("CastorDbProducer")


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(True),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    )
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(-1),
    version = cms.string('Parabolic')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    compatibiltyWith11 = cms.untracked.bool(True),
    useDDD = cms.untracked.bool(False)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer")


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(-1)
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.ecalNextToDeadChannelESProducer = cms.ESProducer("EcalNextToDeadChannelESProducer",
    channelStatusThresholdForDead = cms.int32(12)
)


process.ecalSeverityLevel = cms.ESProducer("EcalSeverityLevelESProducer",
    dbstatusMask = cms.PSet(
        kBad = cms.vstring('kNonRespondingIsolated', 
            'kDeadVFE', 
            'kDeadFE', 
            'kNoDataNoTP'),
        kGood = cms.vstring('kOk'),
        kProblematic = cms.vstring('kDAC', 
            'kNoLaser', 
            'kNoisy', 
            'kNNoisy', 
            'kNNNoisy', 
            'kNNNNoisy', 
            'kNNNNNoisy', 
            'kFixedG6', 
            'kFixedG1', 
            'kFixedG0'),
        kRecovered = cms.vstring(),
        kTime = cms.vstring(),
        kWeird = cms.vstring()
    ),
    flagMask = cms.PSet(
        kBad = cms.vstring('kFaultyHardware', 
            'kDead', 
            'kKilled'),
        kGood = cms.vstring('kGood'),
        kProblematic = cms.vstring('kPoorReco', 
            'kPoorCalib', 
            'kNoisy', 
            'kSaturated'),
        kRecovered = cms.vstring('kLeadingEdgeRecovered', 
            'kTowerRecovered'),
        kTime = cms.vstring('kOutOfTime'),
        kWeird = cms.vstring('kWeird', 
            'kDiWeird')
    ),
    timeThresh = cms.double(2.0)
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalOOTPileupESProducer = cms.ESProducer("OOTPileupDBCompatibilityESProducer")


process.hcalRecAlgos = cms.ESProducer("HcalRecAlgoESProducer",
    DropChannelStatusBits = cms.vstring('HcalCellMask', 
        'HcalCellOff', 
        'HcalCellDead'),
    RecoveredRecHitBits = cms.vstring('TimingAddedBit', 
        'TimingSubtractedBit'),
    SeverityLevels = cms.VPSet(cms.PSet(
        ChannelStatus = cms.vstring(''),
        Level = cms.int32(0),
        RecHitFlags = cms.vstring('')
    ), 
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellCaloTowerProb'),
            Level = cms.int32(1),
            RecHitFlags = cms.vstring('')
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellExcludeFromHBHENoiseSummary'),
            Level = cms.int32(5),
            RecHitFlags = cms.vstring('HSCP_R1R2', 
                'HSCP_FracLeader', 
                'HSCP_OuterEnergy', 
                'HSCP_ExpFit', 
                'ADCSaturationBit', 
                'HBHEIsolatedNoise', 
                'AddedSimHcalNoise')
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring(''),
            Level = cms.int32(8),
            RecHitFlags = cms.vstring('HBHEHpdHitMultiplicity', 
                'HBHEPulseShape', 
                'HOBit', 
                'HFInTimeWindow', 
                'ZDCBit', 
                'CalibrationBit', 
                'TimingErrorBit', 
                'HBHESpikeNoise', 
                'HBHETriangleNoise', 
                'HBHETS4TS5Noise', 
                'HBHEOOTPU')
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring(''),
            Level = cms.int32(11),
            RecHitFlags = cms.vstring('HFLongShort', 
                'HFPET', 
                'HFS8S1Ratio', 
                'HFDigiTime')
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellCaloTowerMask'),
            Level = cms.int32(12),
            RecHitFlags = cms.vstring('HBHEFlatNoise', 
                'HBHENegativeNoise')
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellHot'),
            Level = cms.int32(15),
            RecHitFlags = cms.vstring('')
        ), 
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellOff', 
                'HcalCellDead'),
            Level = cms.int32(20),
            RecHitFlags = cms.vstring('')
        ))
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    appendToDataLabel = cms.string('')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiPixelQualityFromDbRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        ))
)


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(cms.PSet(
        Label = cms.untracked.string(''),
        NormalizationFactor = cms.untracked.double(1.0),
        Record = cms.string('SiStripApvGainRcd')
    ), 
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiStripDetVOffRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.trackerGeometryDB = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.trackerNumberingGeometryDB = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False)
)


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('80X_dataRun2_Prompt_v11')
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.TotemDAQMappingESSourceXML = cms.ESSource("TotemDAQMappingESSourceXML",
    mappingFileNames = cms.untracked.vstring('CondFormats/TotemReadoutObjects/xml/ctpps_210_mapping.xml'),
    maskFileNames = cms.untracked.vstring(),
    verbosity = cms.untracked.uint32(0)
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HERecalibration = cms.bool(False),
    HEreCalibCutoff = cms.double(20.0),
    HFRecalibration = cms.bool(False),
    iLumi = cms.double(-1.0),
    testHFQIE10 = cms.bool(False),
    toGet = cms.untracked.vstring('GainWidths')
)


process.essourceEcalNextToDead = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalNextToDeadChannelRcd')
)


process.essourceEcalSev = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalSeverityLevelAlgoRcd')
)


process.essourceSev = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('HcalSeverityLevelComputerRcd')
)


process.tpparams12 = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalTPGPhysicsConstRcd')
)


process.prefer("es_hardcode")

process.schedule = cms.Schedule(*[ process.NtuplePath, process.NtupleEndPath ])

