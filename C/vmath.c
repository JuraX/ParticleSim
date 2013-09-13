#include <math.h>
#include <stdio.h>
#include "vmath.h"

Vector2d create_vector2d(double x, double y)
{
  Vector2d v = {.x= x, .y= y};
  return v;
}

Vector2d add_vector2d(Vector2d a, Vector2d b)
{
  Vector2d v = {.x= a.x + b.x,.y= a.y + b.y};
  return v;
}

Vector2d sub_vector2d(Vector2d a, Vector2d b)
{
  Vector2d v = {.x= a.x - b.x,.y= a.y - b.y};
  return v;
}

Vector2d div_vector2d(Vector2d a, double f)
{
  Vector2d v = {.x= a.x / f,.y= a.y / f};
  return v;
}

Vector2d mul_vector2d(Vector2d a, double f)
{
  Vector2d v = {.x= a.x * f,.y= a.y * f};
  return v;
}

double distance_sqrd(Vector2d a, Vector2d b)
{
  return (pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
}

double distance(Vector2d a, Vector2d b)
{
  return sqrt(distance_sqrd(a, b));
}

double length_sqrd(Vector2d a)
{
  return (pow(a.x, 2) + pow(a.y, 2));
}

double length(Vector2d a)
{
  return sqrt(length_sqrd(a));
}

Vector2d normalize_vector2d(Vector2d a)
{
  if(a.x == 0 && a.y == 0){ return create_vector2d(0, 0);  }
  return div_vector2d(a, length(a));
}

void print_vector2d(Vector2d a)
{
  printf("(%f,%f)\n", a.x, a.y);
}
