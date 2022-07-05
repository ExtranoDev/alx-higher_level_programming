#include <python.h>

/**
 * print_python_list_info - prints information about a python lists
 * @p: pointer variable to object
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int count, spl, alcl;
	PyObject *pyl_obj;

	spl = Py_SIZE(p);
	alcl = ((PyListObject *)p)->allocated;

	printf("[*] Size of Python List = %d\n", spl);
	printf("[*] Allocated = %d\n", alcl);
	while (count < spl)
	{
		printf("Element %d: ", count);
		pyl_obj = PyList_GetItem(p, count);
		printf("%s\n", py_Type(pyl_obj)->tp_name);
		count++;
	}
}
