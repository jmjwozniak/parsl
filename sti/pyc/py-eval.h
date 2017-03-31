
#pragma once

#include <stdbool.h>

bool python_init(void);

bool python_eval(bool persist, const char* code, const char* expression,
                 char** output);

void python_finalize(void);
