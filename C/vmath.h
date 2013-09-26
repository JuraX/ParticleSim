#ifndef _VMATH_H_
#define _VMATH_H_

typedef struct {
    double x;
    double y;
} Vector2d;

typedef struct {
    double x;
    double y;
    double z;
} Vector3d;

Vector2d create_vector2d(double x, double y);

Vector2d add_vector2d(Vector2d a, Vector2d b);

Vector2d sub_vector2d(Vector2d a, Vector2d b);

Vector2d div_vector2d(Vector2d a, double f);

Vector2d mul_vector2d(Vector2d a, double f);

double distance_sqrd2d(Vector2d a, Vector2d b);

double distance2d(Vector2d a, Vector2d b);

double length_sqrd2d(Vector2d a);

double length2d(Vector2d a);

Vector2d normalize_vector2d(Vector2d a);

void print_vector2d(Vector2d a);


Vector3d create_vector3d(double x, double y, double z);

Vector3d add_vector3d(Vector3d a, Vector3d b);

Vector3d sub_vector3d(Vector3d a, Vector3d b);

Vector3d div_vector3d(Vector3d a, double f);

Vector3d mul_vector3d(Vector3d a, double f);

double distance_sqrd3d(Vector3d a, Vector3d b);

double distance3d(Vector3d a, Vector3d b);

double length_sqrd3d(Vector3d a);

double length3d(Vector3d a);

Vector3d normalize_vector3d(Vector3d a);

void print_vector3d(Vector3d a);

#endif
