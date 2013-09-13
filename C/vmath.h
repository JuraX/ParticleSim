#ifndef _VMATH_H_
#define _VMATH_H_

typedef struct {
    float x;
    float y;
} Vector2d;

Vector2d create_vector2d(float x, float y);

Vector2d add_vector2d(Vector2d a, Vector2d b);

Vector2d sub_vector2d(Vector2d a, Vector2d b);

Vector2d div_vector2d(Vector2d a, float f);

Vector2d mul_vector2d(Vector2d a, float f);

void print_vector2d(Vector2d a);

#endif
