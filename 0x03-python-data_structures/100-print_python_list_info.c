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
	PyListObject *list;
	PyObject *item;
	Py_ssize_t index;

	list = (PyListObject *) p;
	printf("[*] Size of the Python List = %d\n", (int) Py_SIZE(list));
	printf("[*] Allocated = %d\n", (int) list->allocated);

	for (index = 0; index < Py_SIZE(list); index++)
	{
		item = PyList_GetItem(p, index);
		if (item != NULL)
			printf("Element %d: %s\n", (int) index, item->ob_type->tp_name);
	}
}
