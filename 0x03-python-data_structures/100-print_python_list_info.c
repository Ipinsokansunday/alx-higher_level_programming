#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Displays information about a Python list.
 * @p: Pointer to a Python list object.
 *
 * This function prints the size and allocated memory of a Python list, as well
 * as information about each element's type within the list.
 *
 * Return: Void.
 */

void print_python_list_info(PyObject *p)
{
	long int list_size, allocated_memory, i;
	PyObject *element;

	i = 0;
	list_size = PyList_Size(p);
	allocated_memory = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated Memory = %ld\n", allocated_memory);

	while (i < list_size)
	{
		element = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, PyUnicode_AsUTF8(Py_TYPE(element)->tp_name));
		i++;
	}
}
