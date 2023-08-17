#include <Python.h>

/**
* print_python_list - Print basic information about Python lists
* @p: PyObject pointer
*/
void print_python_list(PyObject *p)
{
	Py_ssize_t size;

	size = ((PyVarObject *)p)->ob_size;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	Py_ssize_t i;

	for (i = 0; i < size; ++i)
	{
		PyObject *element = ((PyListObject *)p)->ob_item[i];
		const char *type = element->ob_type->tp_name;

		printf("Element %ld: %s\n", i, type);
	}
}

/**
* print_python_bytes - Print basic information about Python bytes objects
* @p: PyObject pointer
*/
void print_python_bytes(PyObject *p)
{
	char *str;
	Py_ssize_t size;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	printf("  size: %ld\n", size);

	str = ((PyBytesObject *)p)->ob_sval;
	printf("  trying string: %s\n", str);

	printf("  first %ld bytes:", size < 10 ? size : 10);
	Py_ssize_t i;

	for (i = 0; i < size && i < 10; ++i)
	{
		printf(" %02x", (unsigned char)str[i]);
	}
	printf("\n");
}

