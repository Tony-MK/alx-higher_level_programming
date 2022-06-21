#include "Python.h"

/*
 * print_python_list - Prints a Python list
 * @p: Points to a python list object
 *
 */
void print_python_list(PyObject *p)
{
	if (p == NULL)
	{
		printf("Errro");
	}
}

/*
 *
 *
 */
void print_python_bytes(PyObject *p)
{
	if (p == NULL)
	{
		printf("Erro");
	}
}

/*
 * print_python_float - Prints a Python float object
 * @p: Points to a python list object
 *
 */
void print_python_float(PyObject *p)
{
	if (p == NULL)
	{
		printf("Error");
	}
}
