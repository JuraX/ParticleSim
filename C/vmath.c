#include <math.h>
#include <stdio.h>
#include "vmath.h"

Vector2d create_vector2d(float x, float y)
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

Vector2d div_vector2d(Vector2d a, float f)
{
  Vector2d v = {.x= a.x / f,.y= a.y / f};
  return v;
}

Vector2d mul_vector2d(Vector2d a, float f)
{
  Vector2d v = {.x= a.x * f,.y= a.y * f};
  return v;
}

void print_vector2d(Vector2d a)
{
  printf("(%e,%e)\n", a.x, a.y);
}
