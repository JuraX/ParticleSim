#include "vmath.h"

int main(int argc, char *argv[])
{
  Vector2d a = create_vector2d(1, 4);
  Vector2d b = create_vector2d(4, 1);
  Vector2d c = add_vector2d(a, b);
  print_vector2d(a);
  print_vector2d(b);
  print_vector2d(c);
  return 0;
}
