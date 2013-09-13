#include <stdio.h>
#include "vmath.h"

int main(int argc, char *argv[])
{
  Vector2d a = create_vector2d(2, 2);
  print_vector2d(a);
  printf("%e\n", length(a));
  
  a = normalize_vector2d(a);
  print_vector2d(a);
  printf("%e\n", length(a));
  return 0;
}
