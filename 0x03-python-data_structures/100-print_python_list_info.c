#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints python list info
 *
 * @p: PyObject
 * Return: no return
 */
void print_python_list_info(PyObject *p)
{
	long int spl, count;
	PyListObject *obj_list;
	PyObject *item;

	spl = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", spl);

	obj_list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", obj_list->allocated);

	for (count = 0; count < spl; count++)
	{
		item = PyList_GetItem(p, count);
		printf("Element %ld: %s\n", count, Py_TYPE(item)->tp_name);
	}
}
