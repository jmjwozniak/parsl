
#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>

#include "io.h"
#include "py-eval.h"

static void crash(char* fmt, ...);

static void inputs(int argc, char* argv[], char** code, char** expr);

int
main(int argc, char* argv[])
{
  char* code;
  char* expr;
  inputs(argc, argv, &code, &expr);

  python_init();

  // Do Python
  char* result;
  bool rc = python_eval(false, code, expr, &result);
  if (!rc) crash("Python error!");
  printf("%s\n", result);

  // Clean up
  python_finalize();
  free(code);
  free(expr);
  exit(EXIT_SUCCESS);
}

static void
inputs(int argc, char* argv[], char** code, char** expr)
{
  if (argc != 3) crash("Requires 2 input files!");
  char* code_file = argv[1];
  char* expr_file = argv[2];
  *code = slurp(code_file);
  if (*code == NULL) crash("failed to read: %s", code_file);
  *expr = slurp(expr_file);
  if (*expr == NULL) crash("failed to read: %s", expr_file);
  chomp(*code);
  chomp(*expr);
}

static void
crash(char* fmt, ...)
{
  printf("py-eval: ");
  va_list ap;
  va_start(ap, fmt);
  vprintf(fmt, ap);
  printf("\n");
  va_end(ap);
  exit(EXIT_FAILURE);
}
