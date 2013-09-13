#ifndef _PARTICLE_H_
#define _PARTICLE_H_

#include "vmath.h"

#define DENSITY 2960 //kg/m^3

typedef struct {
    double mass;
    double col_radius;
    Vector2d position;
    Vector2d movement;
} Particle;

Particle *create_particle(double mass, double x, double y);

void free_particle(Particle *a);

#endif
