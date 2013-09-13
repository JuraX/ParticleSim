#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "vmath.h"

#include "particle.h"

Particle *create_particle(double mass, double x, double y)
{
  Particle *c = malloc(sizeof(Particle));
  c->mass = mass;
  c->position = create_vector2d(x, y);
  c->movement = mul_vector2d(create_vector2d(-y, x), 0.0005);
  c->col_radius = cbrt(0.75*(mass/DENSITY)/M_PI); //r=sqrt3(0.75*(m/d)/pi)
  return c;
}

void free_particle(Particle *a)
{
  free(a);
}
