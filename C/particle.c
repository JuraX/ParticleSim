#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "vmath.h"

#include "particle.h"

#define GRAVITATION 6.67384e-11
#define COLLOSION_RADIUS_FACTOR 15
#define FACTOR = 10000000000000

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

void calc_movement(Particle a, Particle *field, double dt)
{
  Vector2d force = create_vector2d(0, 0);
  int length = (sizeof(field) / sizeof(Particle));
  int pos;
}
