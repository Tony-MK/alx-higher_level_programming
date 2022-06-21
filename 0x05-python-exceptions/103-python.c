#include "Python.h"

/*
 * print_python_list - Prints a Python list
 * @p: Points to a python list object
 *
 */
void print_python_list(PyObject *p)
{
	printf("[*] Python list info\n ");
	if (!(p && PyList_Check(p)))
		printf("[ERROR] Invalid List Object\n");
	else
		printf(
				"[*] Size of the Python List = %ld\n[*] Allocated = \n",
			       	PyList_Size(p)
			);
}

/*
 * print_python_bytes - Prints a Python bytes object
 * @p: Points to a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
        printf("[.] bytes objecst info\n ");
	if (p && PyBytes_Check(p))
		printf(
				"size: %ld\n trying string: %s\n first bytes: %p\n", 
				PyBytes_Size(p),
				PyBytes_AsString(p),
				PyBytes_AsString(p)
			);
	else
		printf("[ERROR] Invalid Bytes Object\n");
}

/*
 * print_python_float - Prints a Python float object
 * @p: Points to a python list object
 */
void print_python_float(PyObject *p)
{
	printf("[.] float object info\n ");
	if (!(p && PyFloat_Check(p)))
		printf("[ERROR] Invalid Float Object\n");
	else
		printf("value: %f\n", PyFloat_AsDouble(p));
}
