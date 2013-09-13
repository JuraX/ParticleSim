#ifndef _VMATH_H_
#define _VMATH_H_

typedef struct {
    double x;
    double y;
} Vector2d;

Vector2d create_vector2d(double x, double y);

Vector2d add_vector2d(Vector2d a, Vector2d b);

Vector2d sub_vector2d(Vector2d a, Vector2d b);

Vector2d div_vector2d(Vector2d a, double f);

Vector2d mul_vector2d(Vector2d a, double f);

double distance_sqrd(Vector2d a, Vector2d b);

double distance(Vector2d a, Vector2d b);

double length_sqrd(Vector2d a);

double length(Vector2d a);

Vector2d normalize_vector2d(Vector2d a);

void print_vector2d(Vector2d a);

#endif
