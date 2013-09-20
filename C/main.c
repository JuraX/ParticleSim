#include "dbg.h"
#include <stdio.h>
#include "particle.h"

int main(int argc, char *argv[])
{
  Particle *p = create_particle(5, 10, 10);
  check_mem(p);
  free_particle(p);
  
  return 0;
error:
  return 1;
}
