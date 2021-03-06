import FWCore.ParameterSet.Config as cms

TrackAssociatorByHits = cms.ESProducer("TrackAssociatorByHitsESProducer",
    Quality_SimToReco = cms.double(0.5),
    associateRecoTracks = cms.bool(True),
    UseGrouped = cms.bool(True),
    associatePixel = cms.bool(True),
    ROUList = cms.vstring('TrackerHitsTIBLowTof', 
        'TrackerHitsTIBHighTof', 
        'TrackerHitsTIDLowTof', 
        'TrackerHitsTIDHighTof', 
        'TrackerHitsTOBLowTof', 
        'TrackerHitsTOBHighTof', 
        'TrackerHitsTECLowTof', 
        'TrackerHitsTECHighTof', 
        'TrackerHitsPixelBarrelLowTof', 
        'TrackerHitsPixelBarrelHighTof', 
        'TrackerHitsPixelEndcapLowTof', 
        'TrackerHitsPixelEndcapHighTof'),
    UseSplitting = cms.bool(True),
    ComponentName = cms.string('TrackAssociatorByHits'),
    UsePixels = cms.bool(True),
    ThreeHitTracksAreSpecial = cms.bool(True),
    AbsoluteNumberOfHits = cms.bool(False),
    associateStrip = cms.bool(True),
    Purity_SimToReco = cms.double(0.75),
    Cut_RecoToSim = cms.double(0.75),
    SimToRecoDenominator = cms.string('sim') ##"reco"

)


