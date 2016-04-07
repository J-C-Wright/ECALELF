
#ifndef DataFormats_Math_deltaPhi_h
#define DataFormats_Math_deltaPhi_h
#include <cmath>

float reduceRange(x) {

    float o2pi = 1./(2.*M_PI);
    if (std::abs(x) <= (x*o2pi)) return x;
    float n = std::round(x*o2pi);
    return x - n*(2.*M_PI);

}

#endif
