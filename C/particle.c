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

void calc_movement(Particle a, Particle field[], int field_length, double dt)
{
  Vector2d force = create_vector2d(0, 0);
  int length = field_length;
  int pos = 0;

  while(pos < length) {
    Particle b = field[pos];
    if(&b == &a) { continue; } //Keine verechnung mit selbst
    double d = distance_sqrd(a.position, b.position);
    if(sqrt(d) <= a.col_radius) {
      double mass1 = a.mass;
      double mass2 = b.mass;
      a->mass = a.mass + b.mass;
      a->col_radius = cbrt(0.75*(a.mass/DENSITY)/M_PI); //r=sqrt3(0.75*(m/d)/pi)
      a->movement = (a.movement * mass1 = b.movement * mass2) / a.mass;
      free(b);
    }else if(d) {
    }
  }
}
