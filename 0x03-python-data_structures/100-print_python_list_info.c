#include "Python.h"

/**
 * print_python_list_info - Prints information about a Python list
 * @p: Pointer to a Python list
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p), index = 0;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", (((PyListObject *)p)->allocated));

	while (index < size)
	{
		printf(
				"Element %ld: %s\n",
				index,
				((((PyObject *) (PyList_GetItem(p, index)))->ob_type)->tp_name)
		      );
		index++;
	}
}
