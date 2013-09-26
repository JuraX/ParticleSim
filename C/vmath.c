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

double distance_sqrd2d(Vector2d a, Vector2d b)
{
  return (pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
}

double distance2d(Vector2d a, Vector2d b)
{
  return sqrt(distance_sqrd2d(a, b));
}

double length_sqrd2d(Vector2d a)
{
  return (pow(a.x, 2) + pow(a.y, 2));
}

double length2d(Vector2d a)
{
  return sqrt(length_sqrd2d(a));
}

Vector2d normalize_vector2d(Vector2d a)
{
  if(a.x == 0 && a.y == 0){ return create_vector2d(0, 0);  }
  return div_vector2d(a, length2d(a));
}

void print_vector2d(Vector2d a)
{
  printf("(%f,%f)", a.x, a.y);
}


Vector3d create_vector3d(double x, double y, double z)
{
  Vector3d v = {.x= x, .y= y, .z= z};
  return v;
}

Vector3d add_vector3d(Vector3d a, Vector3d b)
{
  Vector3d v = {.x= a.x + b.x, .y= a.y + b.y, .z= a.z + b.z};
  return v;
}

Vector3d sub_vector3d(Vector3d a, Vector3d b)
{
  Vector3d v = {.x= a.x - b.x, .y= a.y - b.y, .z= a.z - b.z};
  return v;
}

Vector3d div_vector3d(Vector3d a, double f)
{
  Vector3d v = {.x= a.x / f, .y= a.y / f, .z= a.z / a.z};
  return v;
}

Vector3d mul_vector3d(Vector3d a, double f)
{
  Vector3d v = {.x= a.x * f, .y= a.y * f, .z= a.z * f};
  return v;
}

double distance_sqrd3d(Vector3d a, Vector3d b)
{
  return (pow(a.x - b.x, 2) + pow(a.y - b.y, 2) + pow(a.z - b.z, 2));
}

double distance3d(Vector3d a, Vector3d b)
{
  return sqrt(distance_sqrd3d(a, b));
}

double length_sqrd3d(Vector3d a)
{
  return (pow(a.x, 2) + pow(a.y, 2) + pow(a.z, 2));
}

double length3d(Vector3d a)
{
  return sqrt(length_sqrd3d(a));
}

Vector3d normalize_vector3d(Vector3d a)
{
  if(a.x == 0 && a.y == 0 && a.z == 0){ return create_vector3d(0, 0, 0);  }
  return div_vector3d(a, length3d(a));
}

void print_vector3d(Vector3d a)
{
  printf("(%f,%f,%f)", a.x, a.y, a.z);
}
