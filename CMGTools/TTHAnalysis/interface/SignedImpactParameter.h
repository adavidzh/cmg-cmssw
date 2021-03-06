#ifndef SignedImpactParmeter_h
#define SignedImpactParmeter_h

#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/GeometryCommonDetAlgo/interface/Measurement1D.h"
struct MagneticField;

class SignedImpactParameter {
    public:
        SignedImpactParameter() ;
        ~SignedImpactParameter() ;

        Measurement1D signedIP3D(const reco::Track &tk, const reco::Vertex &vtx, const reco::Track::Vector jetdir) const ;
        std::pair<double,double> twoTrackChi2(const reco::Track &tk1, const reco::Track &tk2) const ;
    private:
        //MagneticField *bfield_;
        static MagneticField *paramField_;
};


#endif
