#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - get python list info
 * @p: PyObject
 *
 */

void print_python_list_info(PyObject *p)
{
	printf("[*] Size of the Python List = %d\n", (int)(((PyVarObject*)(p))->ob_size));
}
